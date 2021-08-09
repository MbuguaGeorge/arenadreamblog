from django.contrib import admin
from posts.models import *


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Preference)
