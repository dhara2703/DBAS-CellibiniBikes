from django.shortcuts import render

# Create your views here.
def homepage(request):
      return render(request, 'customers/customers_homepage.html')
