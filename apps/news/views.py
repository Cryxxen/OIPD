from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.news.serializers import NewSerializer
from apps.news.models import New


class RetrieveNewApiView(RetrieveAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class ListNewApiView(ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
