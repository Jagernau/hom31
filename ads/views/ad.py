from django.db.models import Q, QuerySet
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)

from ads.permissions import IsCreatedByOrAdminOrModerator
from ads.models import Ad, Category
from rest_framework.request import HttpRequest
from users.models import User

from ads.serializer import (
    AdSerializer,
    AdDetailSerializer,
    AdCreateSerializer,
    AdUpdateSerializer,
    AdImageSerializer,
)


from rest_framework.permissions import IsAuthenticated


class AdListView(ListAPIView):
    queryset: QuerySet[Ad] = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request: HttpRequest, *args, **kwargs):

        categories = request.GET.getlist("cat", default=None)
        catig_qu = None
        for catig_id in categories:
            if catig_qu is None:
                catig_qu = Q(category__id__exact=catig_id)
            else:
                catig_qu |= Q(catigory__id__exact=catig_id)
        if catig_qu:
            self.queryset = self.queryset.filter(catig_qu)

        names = request.GET.get("text", default=None)
        if names:
            self.queryset = self.queryset.filter(name__icontains=names)

        locat = request.GET.get("location", default=None)
        if locat:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=locat
            )

        price_from = request.GET.get("price_from", default=None)
        price_to = request.GET.get("price_to", default=None)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]

class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdImageSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]


class AdDeleteView(DestroyAPIView):
    """Delete ad by id"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
