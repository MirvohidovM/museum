from rest_framework.generics import CreateAPIView, ListAPIView
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import get_language

from .models import Order, ExcursionType
from .serializers import OrderSerializer, ExcursionTypeSerializer


class ExcursionTypeAPIView(ListAPIView):
    queryset = ExcursionType.objects.all()
    serializer_class = ExcursionTypeSerializer


class OrderCreateApiView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        language = get_language()
        if serializer.is_valid():
            serializer.save()
            if language == 'uz':
                send_mail(
                    'Aloqa tarixi muzeyi',
                    'Buyurtmangiz muvaffaqiyatli qabul qilindi. Buyurtmangiz masʼul xodimlar tomonidan 3 ish kunida oʻrganib chiqilib, natijasi boʻyicha tegishli maʼlumot elektron pochtangizga yuboriladi.',
                    settings.EMAIL_HOST_USER,
                    [serializer.data['email']],
                    fail_silently=False,
                )
            elif language == 'uzb':
                send_mail(
                    'Алоқа тарихи музейи',
                    'Буюртмангиз муваффақиятли қабул қилинди. Буюртмангиз масъул ходимлар томонидан 3 иш кунида ўрганиб чиқилиб, натижаси бўйича тегишли маълумот электрон почтангизга юборилади.',
                    settings.EMAIL_HOST_USER,
                    [serializer.data['email']],
                    fail_silently=False,
                )
            elif language == 'ru':
                send_mail(
                    'Музей истории связи',
                    'Ваш заказ успешно принят. Ваш заказ будет рассмотрен ответственными сотрудниками в течение 3 рабочих дней, и соответствующая информация будет отправлена на ваш адрес электронной почты.',
                    settings.EMAIL_HOST_USER,
                    [serializer.data['email']],
                    fail_silently=False,
                )
            else:
                send_mail(
                    'Museum of communication history',
                    'Your order has been successfully received. Your order will be reviewed by the responsible staff within 3 working days and the relevant information will be sent to your email address.',
                    settings.EMAIL_HOST_USER,
                    [serializer.data['email']],
                    fail_silently=False,
                )
            return Response({
                'status': 200,
                'message': 'OK'
            },
            status=status.HTTP_200_OK
            )
        else:
            return Response({
                'status': 400,
                'message': "Validation Error!"
                # 'message': "Buyurtmani to'ldirishda hatolik mavjud"
            },
            status=status.HTTP_400_BAD_REQUEST
            )