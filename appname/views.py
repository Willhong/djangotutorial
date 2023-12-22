from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets

# Create your views here.

def index(request):
    if request.method == 'GET':
        return HttpResponse('this is a GET request')
    elif request.method == 'POST':
        return HttpResponse('this is a POST request')
    
class MyView(APIView):
    def get(self, request):
        # <view logic>
        return HttpResponse('this is a GET request')
    
    def post(self, request):
        # <view logic>
        return HttpResponse('this is a POST request')
    


class Myvieset(viewsets.ViewSet):
    def list(self, request):
        # <view logic>
        return HttpResponse('this is a GET request')
    
    def create(self, request):
        # <view logic>
        return HttpResponse('this is a POST request')