from django.urls import path, include

from report.views import Report

urlpatterns = [
    path('', Report.as_view())
]
