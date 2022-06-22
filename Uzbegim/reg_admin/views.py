from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, \
    RetrieveAPIView
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import Registration, Rooms
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


def calc(request,pk):
    one_room_price = Rooms.objects.get(pk=pk)
    day = Registration.objects.get(rooms_id=pk)
    vis = day.visit_date
    lea = day.leave_date
    price = one_room_price.price
    a = lea - vis
    if a == '0:00:00':
        a = int(1)
        total_price = (a * price)
    else:
        a = int(a.days)
        print(a)
        total_price =(a * price)
        Registration.objects.filter(rooms_id=pk).update(price=int(total_price))
        print(Registration.price)
# def some_view(request):
#     # Создать файлоподобный буфер для приема данных PDF.
#     buffer = io.BytesIO()
#
#     # Создайте объект PDF, используя буфер в качестве его «файла».
#     p = canvas.Canvas(buffer)
#
#     # Рисуйте в PDF. Здесь происходит генерация PDF.
#     # Полный список функций см. в документации ReportLab.
#     p.drawString(1, 1, "Hello world.")
#
#     # Чисто закройте объект PDF, и все готово.
#     p.showPage()
#     p.save()
#
#     # FileResponse устанавливает заголовок Content-Disposition, чтобы браузеры
#     # предоставить возможность сохранить файл.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
