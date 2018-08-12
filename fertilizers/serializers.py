#serializer class converts a model to json data
from rest_framework import serializers
from .models import Product, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company         #This will tell what model you need to serialize
        #fields = ('artist', 'album_title')   #To send only required fields from the model Album
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Product         #This will tell what model you need to serialize

        #fields = ('artist', 'album_title')   #To send only required fields from the model Album
        fields = '__all__'            #This will send all the fields from model Album