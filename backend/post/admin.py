from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Repository)
admin.site.register(Directory)
admin.site.register(File)

