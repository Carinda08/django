from django.db import models
from django.db.models.base import Model

# Create your models here.
class Students(models.Model):
    #id(object)
    #name
    uname = models.CharField(max_length=30, unique=True)
    upwd = models.CharField(max_length=30)
    """
    other type:
    t1 = models.TextField() #* long string 
    t2 = models.DateField()
    t3 = models.DateTimeField()
    t4 = models.BooleanField()
    t5 = models.IntegerField()
    t6 = models.PositiveIntegerField()
    t7 = models.DecimalField()
    t8 = models.ImageField() #* depend on Pillow
    t9 = models.FileField()
    o1 = models.AutoField()
    o2 = models.ForeignKey()   #* 1:n
    o3 = models.ManyToManyField() #* n:n
    o4 = models.EmailField()
    o5 = models.UUIDField()
    """

    def __str__(self) -> str:
        return u"Stu:%s"%self.uname

    """
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
    """