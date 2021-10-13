from django.urls import path
from .views import Register, Login, Logout, VehicleTypeViewset


urlpatterns = [
    path('signup/', Register.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('vehicleTypes/', VehicleTypeViewset.as_view(), name="vehicleTypes"),
    
]