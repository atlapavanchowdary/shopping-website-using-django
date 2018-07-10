from django.contrib import admin

# Register your models here. admin atlapavanchowdary@gmail.com pavan123
from garments.models import FormalShirt

class FormalShirtAdmin(admin.ModelAdmin): # FROM formal admin class we are deriving FormalShirtAdmin(this can be changed)
    list_display=('name','price','stock','desc','availability','created','updated')
    
admin.site.register(FormalShirt,FormalShirtAdmin) #syntax:(old model,new model) which means when we refer formal shirt model in admin panel show FormalShirtAdmin model

from garments.models import CausualShirt

class CausualShirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','desc','availability','created','updated')

admin.site.register(CausualShirt,CausualShirtAdmin)

from garments.models import TShirt

class TShirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','desc','availability','created','updated')

admin.site.register(TShirt,TShirtAdmin)

from garments.models import Trouser

class TrouserAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','desc','availability','created','updated')

admin.site.register(Trouser,TrouserAdmin)

from garments.models import Jean

class JeanAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','desc','availability','created','updated')

admin.site.register(Jean,JeanAdmin)

from garments.models import TrackPant

class TrackPantAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','desc','availability','created','updated')

admin.site.register(TrackPant,TrackPantAdmin)


    