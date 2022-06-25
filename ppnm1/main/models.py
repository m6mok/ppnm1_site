from django.db import models


class GalleryImage(models.Model):
    title = models.TextField('Заголовок')
    description = models.TextField('Описание', null=True, blank=True)
    image = models.ImageField('Изображение')
    position = models.PositiveSmallIntegerField(
        'Позиция в галерее',
        default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ('position',)
