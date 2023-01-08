from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .models import Photo
from .serializers import PhotoListSerializer, PhotoDetailSerializer


class PhotoListCreateAPIView(ListCreateAPIView):
    serializer_class = PhotoListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        metadata = self.request.query_params.dict()
        print(metadata)
        if metadata:
            queryset = Photo.objects.filter(
                    metadata__contains=metadata
                )
            return queryset

        return Photo.objects.all()


class PhotoRetrieveAPIView(RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
