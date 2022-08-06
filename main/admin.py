from django.contrib import admin
from .models import Tutorial, Categoria, Tipo, Sobre, Author, Download


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')


class TipoAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'status')
    
    # Add filters for state and stars
    list_filter = ['category', 'user']

    # Make the Business list searchable by name
    search_fields = ['title']

    # We don't want ids showing up
    exclude = ('id',)
    



admin.site.register(Categoria, CategoryAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Tutorial, PostAdmin)
admin.site.register(Download)
admin.site.register(Sobre)
admin.site.register(Author)
