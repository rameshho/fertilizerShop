#serializer class converts a model to json data
from rest_framework import serializers
from .models import Product, Company

class CompanySerializer(serializers.ModelSerializer):
    #products = serializers.HyperlinkedIdentityField('products', view_name='companies-list', lookup_field='company')
    #products = serializers.HyperlinkedIdentityField('products')

    class Meta:
        model = Company
        fields = ('id', 'Name', 'Amount_To_Pay')


# class ProductSerializer(serializers.ModelSerializer):
#     company = CompanySerializer(required=False)
#     products = serializers.HyperlinkedIdentityField('products', view_name='products-list')
#     # author = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username')
#
#     def get_validation_exclusions(self):
#         # Need to exclude `author` since we'll add that later based off the request
#         exclusions = super(ProductSerializer, self).get_validation_exclusions()
#         return exclusions + ['company']
#
#     class Meta:
#         model = Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'