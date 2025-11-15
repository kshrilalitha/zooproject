from django.contrib import admin
from .models import Animals
from .models import caretaker
from .models import donated_by
 
admin.site.register(Animals)
admin.site.register(caretaker)
admin.site.register(donated_by)

# Register your models here.
