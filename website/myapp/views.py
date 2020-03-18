from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Article, TeamSeason, Match, Round, PlayerSeason, Team
from .helpers import per_round


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
        context['active'] = Round.objects.get(active=True).number

        return context


class TableView(ListView):
    model = TeamSeason
    template_name = "myapp/table.html"
    context_object_name = "teams"
    ordering = ["-points"]

    def get_context_data(self, *args, **kwargs):
        context = super(TableView, self).get_context_data(
            *args, **kwargs)

        active = Round.objects.get(active=True).number
        next = active + 1

        # next match
        next_round_tuples = Match.objects.filter(
            round=next).values_list('team_home__id', 'team_away__id')

        context['next_round_list'] = [
            item for next_round_tuple in next_round_tuples for item in next_round_tuple]

        context["next_round_matches"] = Match.objects.filter(round=next)

        # form (last 5 matches)
        last_matches_tuples = Match.objects.filter(
            round__number__range=(active-4, active)).values_list('team_home__id', 'team_away__id')

        last_matches_list = [
            item for last_matches_tuple in last_matches_tuples for item in last_matches_tuple]

        last_matches_per_round = per_round(last_matches_list, 12)

        context["last_matches_per_round"] = [
            val for val in last_matches_per_round for _ in range(6)]

        context["last_matches"] = Match.objects.filter(
            round__number__range=(active-4, active))

        return context


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
