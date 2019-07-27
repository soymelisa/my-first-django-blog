from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

admin.site.register(Post)
# Para hacer nuestro modelo visible en la página del administrado
