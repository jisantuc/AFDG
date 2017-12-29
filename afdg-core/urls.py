from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers

from userdata import views as user_views
from game import views as game_views

router = routers.SimpleRouter()
router.register(r'^api/user-data', user_views.AFDGUserViewSet)
router.register(r'^api/game', game_views.AFDGGameViewSet)

urlpatterns = [url(r'^admin/', admin.site.urls)] + router.urls
