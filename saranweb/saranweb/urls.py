
from django.contrib import admin
from django.urls import path ,include
from testdeal.views import index
from rest_framework import routers
import testdeal.views


router = routers.DefaultRouter()
router.register("myDeals",testdeal.views.MyDealViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api2/',include(router.urls))


]
