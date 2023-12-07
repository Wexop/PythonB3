from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<str:string>/<int:number>', views.blog, name='blog'),
    path('info/', views.info, name='info'),
]
