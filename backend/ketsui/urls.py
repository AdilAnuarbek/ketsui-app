from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post_list/", views.post_list, name="post_list"),
    path("posts/<slug:slug>/", views.post_detail, name="post_detail"),
    path("hiragana_table/", views.hiragana_table, name="hiragana_table"),
    path("hiragana_table/<str:kana>/", views.hiragana_kana, name="hiragana_kana"),
]