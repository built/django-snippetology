from django.contrib import admin
from models import Snippet
class SnippetAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'content')

admin.site.register(Snippet, SnippetAdmin)

