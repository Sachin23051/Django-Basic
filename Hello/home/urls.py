from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_title= "harry admin page"
admin.site.site_header="harry pages"
admin.site.index_title="Harry admin Page"

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('index/',views.index , name ='home'),
    path('index2',views.index2 , name ='home'),
    path('about',views.about , name ='about'),
    path('services',views.services , name ='services'),
    path('contact',views.contact , name ='contact'),
    path('',views.display,name='dispaly')
]