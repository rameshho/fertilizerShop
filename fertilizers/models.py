from django.db import models
import datetime
from django.utils import timezone

class Company(models.Model):
    Name = models.CharField(max_length=100)
    Amount_To_Pay = models.FloatField()

    def __str__(self):
        return self.Name

class Product(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)#, primary_key=True)
    Seller_name = models.CharField(max_length=100)
    Contact_Number = models.CharField(max_length=13)
    Purchase_Date = models.DateField(("Date"), default=timezone.now())
    Count = models.IntegerField()
    Price_Per_Piece = models.FloatField()
    Total_Amount = models.PositiveIntegerField(default=0,  editable=False)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        #overriding save functionality of database
        # calculate sum before saving.
        #Reference :- https://docs.djangoproject.com/en/1.7/topics/db/models/#overriding-predefined-model-methods
        self.Total_Amount = self.Count * self.Price_Per_Piece
        super(Product, self).save(*args, **kwargs)  # Call the "real" save() method.