from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class (for inline editing in CarMake admin)
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of extra forms to show

# CarModelAdmin class (optional: to customize CarModel admin display)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year']
    list_filter = ['type', 'year']
    
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
