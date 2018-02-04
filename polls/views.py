from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index2(request):
        return HttpResponse("2222,3333")

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")


