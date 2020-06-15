from django.contrib import admin

# Register your models here.
from .models import Cloth
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('name','sizes','description','production_date','slug')

admin.site.register(Cloth,PostAdmin)