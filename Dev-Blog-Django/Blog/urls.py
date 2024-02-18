from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('BlogView/<slug:slug>/', views.view_blog,name='view_blog'),
    path('Contact/',views.contact_page,name='contact'),
    path('About',views.about_page,name='about'),
    path('Thankyou',views.thankyou_page,name='thankyou')

]

