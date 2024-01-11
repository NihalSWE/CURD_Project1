from django.contrib import admin
from django.urls import path,include
from enroll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_show,name="addandshow"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('<int:id>/', views.update, name="update"),

]
