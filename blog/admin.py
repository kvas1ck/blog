from django.contrib import admin

from .models import Post,Category,Tag

# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Tag)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

    ordering = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

    ordering = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'author',
                    'category',
                    'status',
                    'created_at',
                    'published_at',)

    list_display_links = ('title',)
    list_filter = ('status','category','tag','created_at',)
    search_fields = ('title','excerpt','content','author__username')
    prepopulated_fields = {'slug':('title',)}
    filter_horizontal = ('tag',)
    readonly_fields = ('created_at','updated_at')
    list_select_related = ('author','category')
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    list_per_page = 20

    fieldsets = (
        (
            'Main information', 
            {
                'fields':(
                    'title','slug','category','author'
                )
            },
        ),
        (
            'Content',
            {
                'fields':(
                    'excerpt','content','tag'
                )
            },
        ),
        (
            'Publication',
            {
                'fields':(
                    'status','published_at'
                )
            },
        ),
        (
            'Additional information',
            {
                'fields':(
                    'created_at','updated_at'
                ),
                'classes':(
                    'collapse',
                )
            }
        )
    )

admin.site.site_header = 'Personal blog administration'
admin.site.site_title = 'Personal blog admin'
admin.site.index_title = 'Content management'