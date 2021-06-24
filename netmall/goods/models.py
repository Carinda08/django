from django.db import models
from django.db.models.base import Model

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return u'Category%s'%self.name
    

class Goods(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    oldPrice = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(to='Category', on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return u'Goods%s'%self.name


class GoodsDetailName(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return u'GoodsDetailName%s'%self.name



class GoodsDetail(models.Model):
    gdUrl = models.ImageField(upload_to='')
    goodDetailName_id = models.ForeignKey(GoodsDetailName, on_delete=models.DO_NOTHING)
    good_id = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return u'GoodsDetail%s'%self.name


class Size(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return u'Size%s'%self.name



class Color(models.Model):
    name = models.CharField(max_length=30)
    colorUrl = models.ImageField(upload_to='color/')

    def __str__(self) -> str:
        return u'Color%s'%self.name


class Inventory(models.Model):
    count = models.PositiveIntegerField()
    good_id = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)
    color_id = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    size_id = models.ForeignKey(Size, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return u'Inventory%s'%self.name
        

