from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.views import APIView
from docxtpl import DocxTemplate

class Report(APIView):
    permissions_classes = (permissions.AllowAny,)

    @staticmethod
    def get(request):
        cards = request.data
        print(1)

