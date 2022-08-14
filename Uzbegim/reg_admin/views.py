from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, \
    RetrieveAPIView
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import Registration, Rooms
from .serializers import RegSerializer, RegUpdate, RegViews, RegDeteil, Room_Relevant


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

class RoomRel(ListAPIView):
    queryset = Rooms.objects.all()
    serializer_class = Room_Relevant