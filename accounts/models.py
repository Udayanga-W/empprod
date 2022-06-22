import email
from platform import mac_ver
from django.db import models

# Create your models here.
class User(models.Model):
    DEPARTMENTS = (
        ('Collections','Collections'),
        ('Billing','Billing'),
        ('Posting',('Posting'))
    )
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=200,choices=DEPARTMENTS)
    ismanager = models.BooleanField()
    manager_mail = models.EmailField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.email