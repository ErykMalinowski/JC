from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Article, TeamSeason, Match


class ArticleListView(ListView):
    model = Article
    template_name = "myapp/index.html"
    context_object_name = "articles"
    ordering = ["-created"]
    paginate_by = 1

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(
            *args, **kwargs)
        context['matches'] = Match.objects.filter(round__active=True)

        return context


class TableView(ListView):
    model = TeamSeason
    template_name = "myapp/table.html"
    context_object_name = "teams"
    ordering = ["-points"]


class MatchesView(TemplateView):
    template_name = "myapp/matches.html"


class StatsView(TemplateView):
    template_name = "myapp/stats.html"
