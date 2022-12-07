from django.contrib import admin

# Register your models here.
from .models import Clubs

# class CustomClubsAdmin(admin.ModelAdmin):
#     model = Snack
#     list_display=('club_name','trophies','purchaser')
#     list_filter=('club_name','trophies')
    
#     search_fields=('club_name','trophies')
#     fieldsets=(('Owner',{'fields':('purchaser',)}),('snack info',{'fields':('name','desc',)}),)

admin.site.register(Clubs)