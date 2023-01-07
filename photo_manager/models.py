from django.db import models


class Photo(models.Model):
    image = models.ImageField(
                upload_to='images',
                verbose_name='Фотография'
            )
    metadata = models.JSONField(
                verbose_name='Дополнительная информация к фото',
                null=True
            )

    def __str__(self):
        return f'Фото {self.pk}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
