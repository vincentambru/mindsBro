from django.contrib import admin
from .models import blogPage
from .models import dynamicPage
from .models import sliderPage


# Register your models here.

admin.site.register(blogPage)
admin.site.register(dynamicPage)
admin.site.register(sliderPage)

