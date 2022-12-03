
from django.db import models

"""
Модель **объявления** должна содержать следующие поля:

- title — название товара.
- price — цена товара (целое число).
- description — описание товара.
- author — пользователь, который создал объявление.
- created_at — время и дата создания объявления.

*Все записи при выдаче должны быть отсортированы по дате создания 
(чем новее, тем выше).*

Модель **отзыва** должна содержать следующие поля:

- text — текст отзыва.
- author — пользователь, который оставил отзыв.
- ad — объявление, под которым оставлен отзыв.
- created_at - время и дата создания отзыва
"""


class Ad(models.Model):
    title = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ad_images', null=True, blank=True)


class Comment(models.Model):
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
