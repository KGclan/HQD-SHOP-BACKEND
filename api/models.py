from django.db import models

class Tastes(models.Model):
  id = models.AutoField(primary_key=True, verbose_name="Идентификатор")
  name = models.CharField(max_length=128, verbose_name="Название", unique=True)

  def __str__(self):
        return self.name

  class Meta:
    verbose_name_plural = "Вкусы"
    verbose_name = "Вкус"

class Product(models.Model):
  id = models.AutoField(primary_key=True, verbose_name="Идентификатор")
  name = models.CharField(max_length=128, verbose_name="Название", unique=True)
  img = models.ImageField(verbose_name="Картинка")
  description = models.TextField(verbose_name="Описание")
  tastes = models.ManyToManyField(Tastes)

  def __str__(self):
        return self.name

  class Meta:
    verbose_name_plural = "Продукты"
    verbose_name = "Продукт"

