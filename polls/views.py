from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index2(request):
        return HttpResponse("This is a test.")

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")


