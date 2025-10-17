from django.contrib.messages import api
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import TaskViewSet

# urlpatterns = [
#     path("", views.index, name="index"),
#     # path("search/<str:term>/", views.search, name="search"),
#     # path("kanji_search/<str:term>/", views.kanji_search, name="kanji_search"),
#     path('api/', include('api.urls'))
# ]

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [
    path('', include(router.urls)),
]