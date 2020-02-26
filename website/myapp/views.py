from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "myapp/index.html"

class TableView(TemplateView):
    template_name = "myapp/table.html"

class MatchesView(TemplateView):
    template_name = "myapp/matches.html"