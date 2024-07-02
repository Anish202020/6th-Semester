from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)

    def _str_(self):
        return self.name


class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.customer_name