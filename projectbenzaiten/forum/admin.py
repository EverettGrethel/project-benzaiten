from django.contrib import admin
from .models import Post
from .models import Community

admin.site.register(Community)
admin.site.register(Post)
