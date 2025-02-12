# from django.contrib import admin
from django.contrib.gis import admin
# from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from .models import Counties, Raster
# Register your models here.
class CountiesAdmin(LeafletGeoAdmin):
# class CountiesAdmin(OSMGeoAdmin):
    list_display = ('county',)
    # search_fields = ()

    list_filter = ("county",)

class RasterAdmin(admin.ModelAdmin):
    list_display = ('raster_name', 'year','resolution')



admin.site.register(Counties, CountiesAdmin)
admin.site.register(Raster, RasterAdmin)


# from django.contrib.auth.models import User
# user = User.objects.get(username='normaluser')
# user.is_superuser = True
# user.save()

# will list you all super users on the system.
# User.objects.filter(is_superuser=True)

# usr = User.objects.get(username='your username')
# usr.set_password('raw password')
# usr.save()