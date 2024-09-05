from django.contrib import admin

from .models import Car, Client, Sale


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'color', 'mileage', 'volume', 'body_type', 'drive_unit', 'gearbox',
                    'fuel_type', 'price', 'image')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'middle_name', 'date_of_birth', 'phone_number')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('client', 'car', 'created_at')

# зарегистрируйте необходимые модели
