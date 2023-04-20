"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01.views import account, user, department

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),

    path('user/list/', user.user_list),
    path('user/add/', user.user_add),

    path('department/list/', department.department_list),
    path('department/add/', department.department_add),
    path('department/<int:nid>/delete/', department.department_delete),
    path('department/<int:nid>/edit/', department.department_edit),
]
