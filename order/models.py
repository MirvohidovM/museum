from django.db import models
from enum import Enum
from django.db.models.signals import pre_save
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import get_language

from baseapp.models import BaseModel
from config.utils import unique_slug_generator, random_string_generator


class ExcursionLanguage(Enum):
    uz = ["O'zbekcha", "Ўзбекча", "Узбекский", "Uzbek"]
    ru = ["Ruscha", "Русча", "Русский", "Russian"]
    en = ["Inglizcha", "Инглизча", "Английский", "English"]


class ExcursionType(models.Model):
    name = models.CharField(max_length=500, verbose_name='Nomlanishi')

    class Meta:
        db_table = 'excursion_type'
        verbose_name = 'Экскурсия тури'
        verbose_name_plural = 'Экскурсия турлари'

    def __str__(self):
        return self.name


class Order(BaseModel):
    NEW = 1
    APPROVED = 2
    REJECTED = 3
    STATUS_CHOICE = (
        (NEW, 'Янги'),
        (APPROVED, 'Қабул қилинди'),
        (REJECTED, 'Рад этилди'),
    )
    firstname = models.CharField(max_length=254, verbose_name='Исм')
    lastname = models.CharField(max_length=254, verbose_name='Фамилияси')
    email = models.EmailField(max_length=254, verbose_name='Электрон почтаси')
    phone = models.CharField(max_length=30, verbose_name="Боғланиш телефони")
    visit_time = models.DateTimeField(auto_now=True, verbose_name='Ташриф куни ва соати')
    num_visitors = models.IntegerField(default=0, verbose_name='Ташрифчилар сони')
    organization = models.CharField(max_length=500, verbose_name='Муассаса номи')
    excursion_type = models.ForeignKey(ExcursionType, on_delete=models.SET_NULL,
                            null=True, verbose_name='Экскурсия тури')
    excursion_lan = models.CharField(max_length=254, verbose_name='Экскурсия тили',
                        choices=([lan.name, lan.value[0]] for lan in ExcursionLanguage))
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICE, default=1,
                                              verbose_name="Статус")
    reason = models.TextField(null=True, blank=True,
                              verbose_name="Рад этиш сабаби")
    class Meta:
        db_table = 'order'
        verbose_name = 'Онлайн буюртма'
        verbose_name_plural = 'Онлайн буюртмалар'
        ordering = ['visit_time']

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.organization})"

    def save(self, *args, **kwargs):
        change = False

        if not self._state.adding:
            change = True
            prev_obj = Order.objects.get(pk=self.id)

        if change and self.status != prev_obj.status:
            if self.status == 2:  # accepted
                if self.firstname_uz is not None:
                    send_mail(
                        'Aloqa tarixi muzeyi',
                        "Sizning arizangiz qabul qilindi.",
                        settings.EMAIL_HOST_USER,
                        [self.email],
                        fail_silently=False,
                    )
                elif self.firstname_uzb is not None:
                    send_mail(
                        'Алоқа тарихи музейи',
                        "Сизнинг аризангиз қабул қилинди.",
                        settings.EMAIL_HOST_USER,
                        [self.email],
                        fail_silently=False,
                    )
                elif self.firstname_ru is not None:
                    send_mail(
                        'Музей истории связи',
                        "Ваша заявка принята.",
                        settings.EMAIL_HOST_USER,
                        [self.email],
                        fail_silently=False,
                    )
                else:
                    send_mail(
                        'Museum of communication history',
                        "Your application is accepted.",
                        settings.EMAIL_HOST_USER,
                        [self.email],
                        fail_silently=False,
                    )

            elif self.status == 3:  # rejected
                if self.firstname_uz is not None:
                    send_mail(
                        'Aloqa tarixi muzeyi',
                        "Sizning arizangiz qabul qilinmadi. Sabab: " + self.reason,
                        settings.EMAIL_HOST_USER,
                        [self.email],
                        fail_silently=False,
                    )
                elif self.firstname_uzb is not None:
                    send_mail(
                        'Алоқа тарихи музейи',
                        "Сизнинг аризангиз қабул қилинмади. Сабаб: " + self.reason,
                        settings.EMAIL_HOST_USER,
                        [self.email],
                        fail_silently=False,
                    )
                elif self.firstname_ru is not None:
                    send_mail(
                        'Музей истории связи',
                        "Ваша заявка не принята. Причина: " + self.reason,
                        settings.EMAIL_HOST_USER,
                        [self.email],
                        fail_silently=False,
                    )
                else:
                    send_mail(
                        'Museum of communication history',
                        "Your application has not been accepted. Cause: " + self.reason,
                        settings.EMAIL_HOST_USER,
                        [self.email],
                        fail_silently=False,
                    )

        super(Order, self).save(*args, **kwargs)


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        if instance.firstname_uz is not None and instance.firstname_uz != '' and \
                instance.lastname_uz is not None and instance.lastname_uz != '':
            name = f'{instance.lastname_uz}{instance.firstname_uz}'
        elif instance.firstname_uzb is not None and instance.firstname_uzb != '' and \
                instance.lastname_uzb is not None and instance.lastname_uzb != '':
            name = f'{instance.lastname_uzb}{instance.firstname_uzb}'
        elif instance.firstname_ru is not None and instance.firstname_ru != '' and \
                instance.lastname_ru is not None and instance.lastname_ru != '':
            name = f'{instance.lastname_ru}{instance.firstname_ru}'
        elif instance.firstname_en is not None and instance.firstname_en != '' and \
                instance.lastname_en is not None and instance.lastname_en != '':
            name = f'{instance.lastname_en}{instance.firstname_en}'
        else:
            name = random_string_generator(size=4)

        instance.slug = unique_slug_generator(instance, title=name)


pre_save.connect(slug_generator, sender=Order)
