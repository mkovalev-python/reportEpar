import datetime
import json
import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.views import APIView
from docxtpl import DocxTemplate


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Report(APIView):
    permissions_classes = (permissions.AllowAny,)

    @staticmethod
    def get(request):
        cards = json.loads(request.data.get('data'))
        task_list = []
        for _ in cards:
            s = Struct(**_)
            task_list.append(s)
        doc = DocxTemplate("template (2).docx")
        context = {'tasks': task_list}
        doc.render(context)
        src = "Report_" + datetime.datetime.now().strftime(
            "%d_%m_%Y_%H:%M:%S") + ".docx"
        doc.save(src)

        file = open(src, "rb")
        try:
            response = HttpResponse(file.read(), content_type="application/zip")
            response["Content-Disposition"] = f"attachment; filename={file.name}"
            return response
        finally:
            os.remove(src)

