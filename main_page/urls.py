from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name='home') , 
    path('single_blog/<str:pk>', views.single_blog , name='single_blog') , 
    path('single_portfolio/<str:pk>', views.single_portfolio , name='single_portfolio') ,
    path('portfolio/', views.all_portfolio , name='all_portfolio') ,
    path('blog/', views.all_blog , name='all_blog') ,

]
