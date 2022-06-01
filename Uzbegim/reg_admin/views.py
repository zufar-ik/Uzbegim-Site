from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, \
    RetrieveAPIView

from .models import Registration
from .serializers import RegSerializer, RegUpdate, RegViews, RegDeteil


class RegCreate(CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegSerializer


class RegList(ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegViews


class RegUpdater(RetrieveUpdateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegUpdate


class RegDetail(RetrieveAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegDeteil
