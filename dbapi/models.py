from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from mapbox_location_field.models import LocationField
import datetime
import uuid

from django.db.models import JSONField
from django.contrib.postgres.fields import ArrayField



#models
class User(models.Model):
    status_choices = (
        ("A","Active"),
        ("I","Inactive")
    )
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=500)
    
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")
    status = models.CharField(max_length=1, choices = status_choices)

    def __str__(self):
        return "{} -{} -{}".format(self.first_name, self.last_name, self.email)



class VehiclesTypes(models.Model):

    SMALL_DUTY_VEHICLE = 'SDV'
    MEDIUM_DUTY_VEHICLE = 'MDV'
    LARGE_DUTY_VEHICLE = 'LDV'
    SEMI_TRAILER_VEHICLE = 'STV'
    BOX_FREIGHT_VEHICLE = 'BFV'
    DRY_VAN_FREIGHT = 'DVF'
    CONCRETE_TRANSPORT_VEHICLE = 'CTV'
    MOBILE_CRANE_VEHICLE = 'MCV' 

    vehicle_choices = (
        ("SMALL_DUTY_VEHICLE","Small Duty Vehicle"),
        ("MEDIUM_DUTY_VEHICLE","Medium Duty Vehicle"),
        ("LARGE_DUTY_VEHICLE","Large Duty Vehicle"),
        ("SEMI_TRAILER_VEHICLE","Semi Trailer Vehicle"),
        ("BOX_FREIGHT_VEHICLE","Box Freight Vehicle"),
        ("DRY_VAN_FREIGHT","Dry Van Freight Vehicle"),
        ("CONCRETE_TRANSPORT_VEHICLE","Concrete Transport Vehicle"),
        ("MOBILE_CRANE_VEHICLE","Mobile Crane Vehicle"),
    )

    vehicle_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    typeOfVehicle = models.CharField(max_length=50, choices = vehicle_choices,default=SMALL_DUTY_VEHICLE)
    max_capacity = models.DecimalField(max_digits=50,decimal_places=2)
    min_capacity = models.DecimalField(max_digits=50,decimal_places=2)
    bookingFee = models.DecimalField(max_digits=50,decimal_places=2)
    pricePerKm = models.DecimalField(max_digits=50,decimal_places=2)
    pricePerMin = models.DecimalField(max_digits=50,decimal_places=2)
    description = models.CharField(max_length=100)
    vehicle_image = models.ImageField(null=True, blank=True)


