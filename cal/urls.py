from django.urls import path
from cal import views

app_name = 'cal'
urlpatterns = [
    path('calendar/', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
]