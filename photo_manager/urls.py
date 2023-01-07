from django.urls import path

from .views import PhotoListCreateAPIView


urlpatterns = [
        path(
            '',
            PhotoListCreateAPIView.as_view(),
            name='photo_list'
        ),
    ]
