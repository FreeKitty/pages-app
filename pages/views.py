from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    templateName='home.html'
    

# Create your views here.
