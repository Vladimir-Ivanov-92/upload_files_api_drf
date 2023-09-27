from django.db import models


class File(models.Model):
    title = models.CharField(max_length=256, default='No title', unique=True,
                             verbose_name='Название файла')
    file = models.FileField(upload_to='uploads/%Y/%m/%d/',
                            verbose_name='Загруженный файл')
    uploaded_at = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата и время загрузки файла')
    processed = models.BooleanField(default=False, verbose_name='Файл обработан')


    def __str__(self) -> str:
        return self.title
