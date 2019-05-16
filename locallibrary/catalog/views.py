from django.shortcuts import render


#Copied boilerplate

from django.views.generic import TemplateView

# Create your views here.


class Index(TemplateView):
    template_name = "index.html"
index = Index.as_view()