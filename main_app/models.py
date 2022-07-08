from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class GenericDefaultModel(models.Model):
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        abstract = True


class UserRole(Enum):
    USER = 'пользователь'
    AUTHOR = 'автор'

    @classmethod
    def as_choices(cls):
        return (
            (cls.USER.value, 'Пользователь'),
            (cls.AUTHOR.value, 'Автор'),
        )


class CustomUserModel(AbstractUser):
    GENDERS = (
        ('Мужчина', 'мужчина'),
        ('Женщина', 'женщина'),
        ('Другое', 'другое')
    )

    fio = models.CharField('ФИО', max_length=150, default='')
    gender = models.CharField('Пол', max_length=50, choices=GENDERS, default='')
    role = models.CharField('Роль', max_length=50, choices=UserRole.as_choices(), blank=False, null=True,
                            default=UserRole.USER.value)


class Post(GenericDefaultModel):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='posts/image/', blank=True)
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='posts_author',
                               verbose_name='Автор')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']


class Comment(GenericDefaultModel):
    user = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, null=True, related_name='user_comments',
                             verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField('Текст комментария', max_length=1000)
    comment_reply = models.ForeignKey('self', related_name='replies', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']
