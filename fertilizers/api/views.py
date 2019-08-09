from fertilizers.models import Product, Company
from .serializers import ProductSerializer, CompanySerializer
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from rest_framework.permissions import IsAuthenticated  # <-- Here


class ProductList(APIView):
    permission_classes = (IsAuthenticated,)  # <-- And here
    def get_object(self, company):
        try:
            return Product.objects.filter(company__Name=company)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, company, format=None):    #
        #Below is the query set :- https://docs.djangoproject.com/en/2.1/topics/db/queries/
        #It will fetch the products belonging to particular company
        products = self.get_object(company)

        #This will tell you what objects you want to serialize
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, company):
        company = Company.objects.get(Name=company)
        data = request.data
        data["company"] = company.id
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Access companies list through this api  http://127.0.0.1:8000/companies/?format=api
class CompanyList(APIView):
    permission_classes = (IsAuthenticated,)  # <-- And here
    #model = Company
    def get(self, request):
        companies = Company.objects.all()

        #This will tell you what objects you want to serialize
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        #serializer = CompanySerializer(data=request.data, files=request.FILES)
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

