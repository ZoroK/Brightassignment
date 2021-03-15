from django.db import models

# Create your models here.


class User(models.Model):
    email= models.EmailField()
    password= models.CharField(max_length=10)
    logged_in=models.BooleanField(default=False)

    # access_token = models.CharField(max_length=100)
    access_token= models.CharField(max_length=100,null=True,blank=True)
    item_id= models.CharField(max_length=100,null=True,blank=True)



