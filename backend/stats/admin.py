from django.contrib import admin
from .models import *

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(SavedPost)
admin.site.register(Follow)

