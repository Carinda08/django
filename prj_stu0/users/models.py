from django.db import models
from django.db.models.base import Model

# Create your models here.
class Students(models.Model):
    #id(object)
    #name
    uname = models.CharField(max_length=30, unique=True)
    upwd = models.CharField(max_length=30)

    def __str__(self) -> str:
        return u"Stu:%s"%self.uname