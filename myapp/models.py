from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Bus(models.Model):
    bus_no = models.IntegerField()
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    total_km = models.DecimalField(decimal_places=0, max_digits=10)
    travel_time = models.DecimalField(decimal_places=2, max_digits=10)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField()
    time = models.TimeField()

    def save(self, *args, **kwargs):
        self.source = self.source.upper()
        self.dest = self.dest.upper()
        super(Bus, self).save(*args, **kwargs)

    def __str__(self):
        return self.bus_name


class Train(models.Model):
    train_no = models.IntegerField()
    train_name = models.CharField(max_length=50)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=4)
    total_km = models.DecimalField(decimal_places=2, max_digits=6)
    travel_time = models.DecimalField(decimal_places=2, max_digits=10)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def save(self, *args, **kwargs):
        self.source = self.source.upper()
        self.dest = self.dest.upper()
        super(Train, self).save(*args, **kwargs)

    def __str__(self):
        return self.train_name
 
    

class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=datetime.now)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password','email']
    def __str__(self):
        return self.name

