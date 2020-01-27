from django.urls import path
from mysite import views

app_name = 'mysite'
urlpatterns = [
    path('', views.defpage, name='defpage'),
    path('index/', views.index, name='index'),
    path('index/<int:question_num>/', views.detail, name='detail'),
    path('index/<int:question_num>/vote', views.vote, name='vote'),
    path('index/<int:question_num>/result', views.result, name='result'),
]