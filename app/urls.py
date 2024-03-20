from django.contrib import admin
from django.urls import path, include
from app.routes import router
urlpatterns = [
   
    path('emp/', include(router.urls)),
]
