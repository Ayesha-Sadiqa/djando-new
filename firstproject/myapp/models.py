from django.db import models
 
class contactus (models.Model):
  firstname=models.CharField(max_length=20)
  lastname=models.CharField(max_length=20)
  message=models.CharField(max_length=100)


