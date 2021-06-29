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
        

class BookInfo(models.Model):
    title = models.CharField(max_length=20, verbose_name='Title')
    date = models.DateField(verbose_name='Date')
    readCnt = models.IntegerField(default=0, verbose_name='TotalRead')
    cmntCnt = models.IntegerField(default=0, verbose_name='TotalComment')
    is_del = models.BooleanField(default=0, verbose_name='isDel')

    def __str__(self) -> str:
        return u'BookInfo_%s'%self.title

    class Meta:
        db_table = 'tb_BookInfo'
        managed = True
        verbose_name = 'BookInfo'
        verbose_name_plural = 'BookInfo'


class HeroInfo(models.Model):
    Gender_Choice = (
        (0, 'female'),
        (1, 'male')
    )

    name = models.CharField(max_length=20, verbose_name='Name')
    gender = models.SmallIntegerField(choices=Gender_Choice, default=0, verbose_name="Gender")
    cmnt = models.CharField(max_length=200, null=True, verbose_name="Comment")
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name="inBook")

    def __str__(self) -> str:
        return u'HeroInfo_%s'%self.name

    class Meta:
        db_table = 'tb_HeroInfo'
        managed = True
        verbose_name = 'HeroInfo'
        verbose_name_plural = 'HeroInfo'

