import factory

from ads.models import Ad, Category
from users.models import User



class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = 'password'



class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Test"
    price = 10

    is_published = False
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
