from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Article, TeamSeason, Match, Round, PlayerSeason


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
        context['active'] = Round.objects.filter(active=True)[0].number

        return context


class TableView(ListView):
    model = TeamSeason
    template_name = "myapp/table.html"
    context_object_name = "teams"
    ordering = ["-points"]


class MatchesView(ListView):
    model = Match
    template_name = "myapp/matches.html"
    context_object_name = "matches"
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super(MatchesView, self).get_context_data(
            *args, **kwargs)
        context['rounds'] = Round.objects.all()

        return context


class StatsView(ListView):
    model = PlayerSeason
    template_name = "myapp/stats.html"

    def get_context_data(self, *args, **kwargs):
        context = super(StatsView, self).get_context_data(
            *args, **kwargs)
        context['scorers'] = PlayerSeason.objects.order_by('-goals')[:5]
        context['assistants'] = PlayerSeason.objects.order_by('-assists')[:5]
        context['total'] = PlayerSeason.objects.order_by('-total')[:5]

        return context
