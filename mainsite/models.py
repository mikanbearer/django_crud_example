from django.db import models
from django.core import validators

# Create your models here.
class Linkman(models.Model):
    SEX_CHOICES = (
        (1, '男'),
        (2, '女'),
    )

    name = models.CharField(
        verbose_name='姓名',
        max_length=15
    )

    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )

    tel = models.CharField(
        verbose_name='電話',
        max_length=15
    )

    email = models.EmailField(
        verbose_name='電子郵件',
        validators=[validators.EmailValidator]
    )

    created_at = models.DateTimeField(
        verbose_name='建立日',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='更新日',
        auto_now=True
    )