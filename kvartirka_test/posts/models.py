from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Post(models.Model):
    text = models.CharField('Текст', max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text


class Comment(MPTTModel):
    text = models.CharField('Текст', max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='children',
        verbose_name='Родительский комментарий')

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.text} -> {self.parent}'
