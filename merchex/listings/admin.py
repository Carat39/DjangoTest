from django.contrib import admin

from listings.models import Band,Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name','year_formed','genre') #Ce qu'on affiche dans l'admin

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','year','type','band') #Ce qu'on affiche dans l'admin

admin.site.register(Band,BandAdmin)
admin.site.register(Listing,ListingAdmin)


