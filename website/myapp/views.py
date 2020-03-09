from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "myapp/index.html"
    context_object_name = "articles"
    ordering = ["-created"]


class TableView(TemplateView):
    template_name = "myapp/table.html"


class MatchesView(TemplateView):
    template_name = "myapp/matches.html"


class StatsView(TemplateView):
    template_name = "myapp/stats.html"
