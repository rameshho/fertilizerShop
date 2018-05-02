from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product         #This will tell what model you need to serialize
        #fields = ('artist', 'album_title')   #To send only required fields from the model Album
        fields = '__all__'            #This will send all the fields from model Album