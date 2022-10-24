from django.urls import path
from rest_framework import routers
from ads.views import (
    AdListView,
    AdDetailView,
    AdUpdateView,
    AdImageView,
    AdDeleteView,
    AdCreateView,
    CategoryListView,
    CategoryDetailView,
    CategoryUpdateView,
    CategoryDeleteView,
    CategoryCreateView,
    index,
    SelectionCreateView,
    SelectionDeleteView,
    SelectionDetailView,
    SelectionUpdateView,
    SelectionListView,
)
from ads.views.location import LocatViewSet


router = routers.SimpleRouter()
router.register("location", LocatViewSet)

urlpatterns = [
    path("", index),
    path("ad/", AdListView.as_view()),
    path("ad/<int:pk>/", AdDetailView.as_view()),
    path("ad/<int:pk>/update/", AdUpdateView.as_view()),
    path("ad/<int:pk>/upload_image/", AdImageView.as_view()),
    path("ad/<int:pk>/delete/", AdDeleteView.as_view()),
    path("ad/create/", AdCreateView.as_view()),
    path("cat/", CategoryListView.as_view()),
    path("cat/<int:pk>/", CategoryDetailView.as_view()),
    path("cat/<int:pk>/update/", CategoryUpdateView.as_view()),
    path("cat/<int:pk>/delete/", CategoryDeleteView.as_view()),
    path("cat/create/", CategoryCreateView.as_view()),
    path("cat/create/", CategoryCreateView.as_view()),
    path("selection/", SelectionListView.as_view()),
    path("selection/<int:pk>/", SelectionDetailView.as_view()),
    path("selection/<int:pk>/update/", SelectionUpdateView.as_view()),
    path("selection/<int:pk>/delete/", SelectionDeleteView.as_view()),
    path("selection/create/", SelectionCreateView.as_view()),
]

urlpatterns += router.urls
