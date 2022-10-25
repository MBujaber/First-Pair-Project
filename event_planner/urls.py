"""event_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from users.views import user_register, logout_user, login_user, home, edit_profile
from events.views import create_event, get_events, update_event_item, delete_event_item, get_event


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("register/", user_register, name="register"),
    path("logout/", logout_user, name="logout"),
    path("login/", login_user, name="login"),
    path("profile/", edit_profile, name="profile"),
    path("event/<int:item_id>/", get_event, name="event-detail"),
    path("events/", get_events, name="event-list"),
    path("events/create/", create_event, name="create-event"),
    path("events/update/<int:item_id>/",
         update_event_item, name="update-event-item"),
    path("events/delete/<int:item_id>/",
         delete_event_item, name="delete-event-item"),


]
