from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete = models.CASCADE, blank = True)
    design = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    collected_price = models.PositiveIntegerField()
    base_price = models.PositiveIntegerField()
    shipping_mode = models.CharField(max_length=250, null = True)
    is_refered = models.BooleanField(default = False)
    date = models.DateField(default = datetime.date.today())

    def __str__(self):
        return self.design + '/' + self.model +'/'+ self.user.username
