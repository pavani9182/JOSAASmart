from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('branch_analysis/',views.Branch_analysis,name="branch_analysis"),
    path('Institute_analysis/',views.Institute_analysis,name="Institute_analysis"),
    path('trendsoveryears/',views.trendsoveryears,name="trendsoveryears"),
    path('trendsOverRounds/',views.trendsOverRounds,name="trendsOverRounds"),
    path('rank_input/',views.rank_input,name="rank_input"),
    path('top10Trends/',views.top10Trends,name="top10Trends"),
]
