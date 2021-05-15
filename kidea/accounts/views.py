from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
	return render(request, 'accounts/index.html')

def login(request):
	return render(request, 'accounts/login.html')

def register(request):
	return render(request, 'accounts/register.html')

def browse(request):
	return render(request, 'accounts/browse.html')

def quotation(request):
	return render(request, 'accounts/quotation.html')

def singleproduct(request):
	return render(request, 'accounts/singleproduct.html')

def systemcabinetQuotation(request):
	return render(request, 'accounts/systemcabinetQuotation.html')




