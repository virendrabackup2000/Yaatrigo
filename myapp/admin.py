from django.contrib import admin
from .models import Bus, Train

# Register your models here.

admin.site.register(Bus)
# admin.site.register(User)
admin.site.register(Train)


admin.site.site_header  = 'YAATRIGO'