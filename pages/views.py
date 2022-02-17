from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from pages import models, serializers, tasks


# Create your views here.
class PageListView(generics.ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = serializers.PageSerializer
    queryset = models.Page.objects.all()


class PageView(generics.RetrieveAPIView):
    queryset = models.Page.objects.all()
    serializer_class = serializers.RetrievePageSerializer

    def get(self, request, *args, **kwargs):
        tasks.increase_counter.delay(self.get_object().id)
        return super().get(request, *args, **kwargs)

