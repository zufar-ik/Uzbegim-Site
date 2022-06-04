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

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def some_view(request):
    # Создать файлоподобный буфер для приема данных PDF.
    buffer = io.BytesIO()

    # Создайте объект PDF, используя буфер в качестве его «файла».
    p = canvas.Canvas(buffer)

    # Рисуйте в PDF. Здесь происходит генерация PDF.
    # Полный список функций см. в документации ReportLab.
    p.drawString(1, 1, "Hello world.")

    # Чисто закройте объект PDF, и все готово.
    p.showPage()
    p.save()

    # FileResponse устанавливает заголовок Content-Disposition, чтобы браузеры
    # предоставить возможность сохранить файл.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')