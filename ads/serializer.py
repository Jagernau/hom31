from rest_framework import serializers
from ads.models import Ad, Category, Location
from users.models import User
from rest_framework.generics import get_object_or_404

from ads.models.selection import Selection

from ads.validator import check_not_publish


class LocatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# AdSerializer
class AdSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        required=False, queryset=Category.objects.all(), slug_field="name"
    )

    author = serializers.SlugRelatedField(
        required=False, queryset=User.objects.all(), slug_field="username"
    )

    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False, read_only=True, slug_field="username"
    )

    category = serializers.SlugRelatedField(
        required=False, read_only=True, slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)
    name = serializers.CharField(allow_blank=False, min_length=10, max_length=100)
    price = serializers.IntegerField(min_value=0, default=0)

    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='username'
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    is_published = serializers.BooleanField(default=None, validators=[check_not_publish])

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._author_id = self.initial_data.pop('author_id')
        self._category_id = self.initial_data.pop('category_id')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(
                name=validated_data.get('name'),
                price=validated_data.get('price'),
                description=validated_data.get('description'),
                is_published=validated_data.get('is_published')
        )
        ad.author = get_object_or_404(User, pk=self._author_id)
        ad.category = get_object_or_404(Category, pk=self._category_id)
        ad.save()

        return ad





class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    category = serializers.SlugRelatedField(
        required=False, queryset=Category.objects.all(), slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        self._category_id = self.initial_data.pop("category_id")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()
        ad.category = get_object_or_404(Category, pk=self._category_id)
        ad.save()

        return ad


class AdImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    is_published = serializers.BooleanField(read_only=True)

    class Meta:
        model = Ad
        fields = "__all__"


# SelectionSerializer
class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Selection
        fields = "__all__"
