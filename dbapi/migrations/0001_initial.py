# Generated by Django 3.2.5 on 2021-09-26 11:15

from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=500)),
                ('ifLogged', models.BooleanField(default=False)),
                ('token', models.CharField(default='', max_length=500, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='VehiclesTypes',
            fields=[
                ('vehicle_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('typeOfVehicle', models.CharField(choices=[('SMALL_DUTY_VEHICLE', 'Small Duty Vehicle'), ('MEDIUM_DUTY_VEHICLE', 'Medium Duty Vehicle'), ('LARGE_DUTY_VEHICLE', 'Large Duty Vehicle'), ('SEMI_TRAILER_VEHICLE', 'Semi Trailer Vehicle'), ('BOX_FREIGHT_VEHICLE', 'Box Freight Vehicle'), ('DRY_VAN_FREIGHT', 'Dry Van Freight Vehicle'), ('CONCRETE_TRANSPORT_VEHICLE', 'Concrete Transport Vehicle'), ('MOBILE_CRANE_VEHICLE', 'Mobile Crane Vehicle')], default='SDV', max_length=50)),
                ('max_capacity', models.DecimalField(decimal_places=2, max_digits=50)),
                ('min_capacity', models.DecimalField(decimal_places=2, max_digits=50)),
                ('bookingFee', models.DecimalField(decimal_places=2, max_digits=50)),
                ('pricePerKm', models.DecimalField(decimal_places=2, max_digits=50)),
                ('pricePerMin', models.DecimalField(decimal_places=2, max_digits=50)),
                ('description', models.CharField(max_length=100)),
                ('vehicle_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
