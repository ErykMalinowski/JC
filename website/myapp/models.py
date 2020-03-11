from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    round = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    goals = models.TextField(blank=True)
    squad = models.TextField()
    cards = models.TextField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Season(models.Model):
    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}/{}".format(self.start_year, self.end_year)


class Round(models.Model):
    number = models.PositiveSmallIntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return "{}. kolejka".format(self.number)


class Team(models.Model):
    name = models.CharField(max_length=40)
    img = models.FileField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    team_home = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team_home")
    team_away = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team_away")
    score_home = models.PositiveSmallIntegerField(null=True, blank=True)
    score_away = models.PositiveSmallIntegerField(null=True, blank=True)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)

    def __str__(self):
        if self.score_home and self.score_away:
            return "{}-{} {}:{}".format(self.team_home.name, self.team_away.name, self.score_home, self.score_away)
        else:
            return "{}-{} -:-".format(self.team_home.name, self.team_away.name)

    # + logika


class Player(models.Model):
    personal_details = models.CharField(max_length=40)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.personal_details


class TeamSeason(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    matches = models.PositiveSmallIntegerField()
    wins = models.PositiveSmallIntegerField()
    draws = models.PositiveSmallIntegerField()
    losses = models.PositiveSmallIntegerField()
    goals_for = models.PositiveSmallIntegerField()
    goals_against = models.PositiveSmallIntegerField()
    points = models.SmallIntegerField()

    def __str__(self):
        return self.team.name


class PlayerSeason(models.Model):
    goals = models.PositiveSmallIntegerField(null=True)
    assists = models.PositiveSmallIntegerField(null=True)
    yellow_cards = models.PositiveSmallIntegerField(null=True)
    red_cards = models.PositiveSmallIntegerField(null=True)
    conceded = models.PositiveSmallIntegerField(null=True)
    clean_sheets = models.PositiveSmallIntegerField(null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.player.personal_details
