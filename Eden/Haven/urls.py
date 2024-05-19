from django.urls import path
from . import views
from .views import DiaryDetailView, DiaryPageView


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('diary/', DiaryPageView.as_view(), name='diary_list'),
    path('diary/<int:pk>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/<int:pk>/update', views.DiaryUpdateView.as_view(), name='diary_update'),
    path('diary/<int:pk>/delete/', views.DiaryDeleteView.as_view(), name='diary_delete'),
    path('diary/create', views.DiaryCreateView.as_view(), name='diary_create'),

]
