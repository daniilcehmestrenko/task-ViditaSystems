from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView

from .models import Photo
from .serializers import PhotoSerializer


class PhotoListCreateAPIView(ListCreateAPIView):
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        metadata = self.request.query_params
        if metadata:
            queryset = Photo.objects.filter(
                    metadata__contains=metadata
                )
            return queryset

        return Photo.objects.all()
