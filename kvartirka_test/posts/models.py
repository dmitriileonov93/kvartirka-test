from django.db import models


class Post(models.Model):
    text = models.CharField('Текст', max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.text


class Comment(models.Model):
    text = models.CharField('Текст', max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='children',
        verbose_name='Родительский комментарий'
    )
    depth_level = models.PositiveIntegerField(default=1, editable=False)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def save(self, *args, **kwargs):
        if self.parent:
            self.depth_level = self.parent.depth_level + 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.text} -> {self.parent}'
