from django.db import models  
  
# Create your models here.  
  
class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  
  
    def _str_(self):  
        return "%s %s" % (self.first_name, self.last_name)