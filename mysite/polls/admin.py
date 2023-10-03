from django.contrib import admin

# Register your models here.
from .models import Question,Drink

admin.site.register(Question)
admin.site.register(Drink)


