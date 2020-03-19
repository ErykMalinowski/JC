"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import ArticleListView, TableView, MatchesView, StatsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleListView.as_view(), name="home"),
    path('table/', TableView.as_view(), name="table"),
    path('matches/', MatchesView.as_view(), name="matches"),
    path('stats/', StatsView.as_view(), name="stats"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# ERRORS
handler400 = 'myapp.views.handler400'
handler403 = 'myapp.views.handler403'
handler404 = 'myapp.views.handler404'
handler500 = 'myapp.views.handler500'
