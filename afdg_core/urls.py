from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers

from game import views as game_views
from userdata import views as user_views

router = routers.SimpleRouter()
router.register(r'^api/game', game_views.AFDGGameViewSet)
router.register(r'^api/authenticate', user_views.UserViewSet)
router.register(r'^api/user-records', user_views.UserWinTrackerViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls)
] + router.urls
