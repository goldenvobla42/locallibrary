from django.contrib import admin
from catalog.models import *

# Register your models here.
#admin.site.register(Song)
#admin.site.register(Author)
admin.site.register(Genre)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Song using the decorator
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'lyrics', 'translation')

