from django.db import models

# Create your models here.
class customerReview(models.Model):
    user_name=models.CharField(max_length=100) #model for storing user name
    bran_name=models.CharField(max_length=100)  #model for storing brand name
    produ_name=models.CharField(max_length=100)  #model for storing product name
    review_data=models.TextField()  

    