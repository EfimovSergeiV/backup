from django.db import models
from uuid import uuid4


def protected_files(instance, filename):
    """ Генерация имени файла """
    print(instance, filename)

    ext = filename.split('.')[-1]
    filename = f"{ instance.uuid }.{ ext }"
    return f"bkps/{ filename }"


class BackupModel(models.Model):
    """ Модель резервных копий """

    uuid = models.UUIDField(default=uuid4, editable=False, unique=True, verbose_name='UUID', primary_key=True)
    service = models.CharField(max_length=255, verbose_name='Сервис')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    file = models.FileField(upload_to=protected_files, verbose_name='Файл', null=True, blank=True,)

    class Meta:
        verbose_name = 'Резервная копия'
        verbose_name_plural = 'Резервные копии'

    def __str__(self):
        return f"{ self.service } { str(self.created_at.strftime('%d.%m.%Y %H:%M')) }"