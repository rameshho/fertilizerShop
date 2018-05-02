from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from django.views import generic, View
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from .models import Product, Company
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from django_tables2 import RequestConfig
from rest_framework import status
from .tables import CompanyTable
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .forms import UserForm, CompanyForm, ProductForm

class IndexViewCompany(generic.ListView):
    template_name = 'fertilizers/index.html'
    context_object_name = 'all_companies'

    def get_queryset(self):
        return Company.objects.all()

def company_list(request):
    table = CompanyTable(Company.objects.all())
    return render(request, 'fertilizers/index.html', {'table': table})

class DetailViewCompany(generic.DetailView):
    model = Company
    template_name = 'fertilizers/detail.html'

    def dispatch(self, request, *args, **kwargs):
        try:

            self.company = Company.objects.get(id=self.kwargs['pk'])
        except Exception as err:
            print("Got error while fetching {}, {}".format(err, self.kwargs['pk']))
        return super(DetailViewCompany, self).dispatch(request, *args, **kwargs)


class CreateViewCompany(CreateView):
    #By default createview will cal <model_name>_form.html template, so in this case it will call company_form.html template
    model = Company
    fields = ['Name', 'Amount_To_Pay']
    #form_class = Company
    success_url = reverse_lazy('fertilizers:index')


class UpdateViewCompany(UpdateView):
    model = Company
    fields = ['Name', 'Amount_To_Pay']

    success_url = reverse_lazy('fertilizers:index')

class DeleteViewCompany(DeleteView):
    model = Company
    #fields = ['Name', 'Amount_To_Pay']
    success_url = reverse_lazy('fertilizers:index')


class CreateViewProduct(CreateView):
    #By default createview will cal <model_name>_form.html template, in this case, will call product_form html template
    model = Product
    fields = ['Name', 'Seller_name', 'Contact_Number', 'Count', 'Price_Per_Piece',]# 'Total_Amount']

    def get_success_url(self):
        return reverse_lazy('fertilizers:Detail-company', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        form.instance.company = Company.objects.get(id=self.kwargs.get('pk'))
        return super(CreateViewProduct, self).form_valid(form)


class UpdateViewProduct(UpdateView):
    model = Product
    parent_model = Company
    fields = ['Name', 'Seller_name', 'Contact_Number', 'Count', 'Price_Per_Piece',]

    def get_success_url(self):
        obj = self.get_object()
        return reverse_lazy('fertilizers:Detail-company', kwargs={'pk': obj.company.id})


class DeleteViewProduct(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse_lazy('fertilizers:Detail-company', kwargs={'pk': self.kwargs.get('pk')})

class UserFormView(View):
    '''What is the blue print of the form'''
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #Fill the form and post it. process form data
    def post(self, request):
        form = self.form_class(request.Post)

        if form.is_valid():
            #It creates an object from the form, and it doesn't save it to database.
            user = form.save()

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.username = 'Ramesh'
            user.set_password(password)

            #This will save user to database
            user.save()

            #returns User Objects if credentials are correct.
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('fertilizers:index')

        return render(request, self.template_name, {'form': form})

class AlbumList(APIView):
    def get(self, request):
        Albums = Product.objects.all()
        serializer = ProductSerializer(Product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)