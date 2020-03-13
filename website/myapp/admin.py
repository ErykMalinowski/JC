from django.contrib import admin
from .models import Article, Season, Round, Team, Match, Player, TeamSeason, PlayerSeason

admin.site.register(Article)
admin.site.register(Season)
admin.site.register(Round)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(TeamSeason)
admin.site.register(PlayerSeason)
