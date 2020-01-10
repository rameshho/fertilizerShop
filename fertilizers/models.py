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
    Date = models.DateField(default=datetime.date.today)
    Name = models.CharField(max_length=100)#, primary_key=True)

    def __str__(self):
        return self.Name

class ProductDetails(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    #Contact_Number = models.CharField(max_length=13)
    Date = models.DateField(default=datetime.date.today)
    #Name = models.CharField(max_length=100)#, primary_key=True)
    Opening_Balance = models.IntegerField()
    Receipt = models.IntegerField()
    Total = models.PositiveIntegerField(default=0,  editable=False)
    Sale = models.IntegerField()
    Closing_Balance = models.IntegerField(default=0,  editable=False)
    Invoice_Number = models.CharField(max_length=13)
    # Count = models.IntegerField()
    # Price_Per_Piece = models.FloatField()
    # Total_Amount = models.PositiveIntegerField(default=0,  editable=False)

    def __str__(self):
        return self.Invoice_Number

    def save(self, *args, **kwargs):
        #overriding save functionality of database
        # calculate sum before saving.
        #Reference :- https://docs.djangoproject.com/en/1.7/topics/db/models/#overriding-predefined-model-methods
        self.Total = self.Opening_Balance + self.Receipt
        self.Closing_Balance = self.Total - self.Sale
        #self.Total_Amount = self.Count * self.Price_Per_Piece
        super(ProductDetails, self).save(*args, **kwargs)  # Call the "real" save() method.