from django.urls import path

from .views import PhotoListCreateAPIView, PhotoRetrieveAPIView


urlpatterns = [
        path(
            '',
            PhotoListCreateAPIView.as_view(),
            name='photo_list'
        ),
        path(
            '<int:pk>/',
            PhotoRetrieveAPIView.as_view(),
            name='photo_list'
        ),
    ]
