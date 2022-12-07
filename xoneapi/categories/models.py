from django.db import models

from user.models import User


class Category(models.Model):
    name_of_category = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.name_of_category}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class BasicCategory(models.Model):
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.categories}'

    class Meta:
        verbose_name = 'BasicCategory'
        verbose_name_plural = 'BasicCategories'


class UserCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.category}'

    class Meta:
        verbose_name = 'UserCategory'
        verbose_name_plural = 'UserCategories'
