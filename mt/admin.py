#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
from django.contrib import admin
from .models import Asset, AssetTransaction, Person, Genre


class DirectorInline(admin.StackedInline):
    model = Person


class ActorInline(admin.StackedInline):
    model = Person


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('title', 'upc', 'genre',)
    list_filter = ('genre',)
    ordering = ('title', 'upc')
    # inlines = [
    #     DirectorInline,
    #     ActorInline,
    # ]
    save_as = True
    fieldsets = (
        ("Title Values", {
            'fields': ('title', 'upc', 'asin', 'url',
                       'release_date', 'publication_date',
                       'genre')
        },),
        ("Misc", {
            # 'classes': ('collapse', ),
            'fields': ('binding', 'brand', 'features',
                       'price', 'list_price', 'currency',
                       'sales_rank'),
        }),
        ("Images", {
            'classes': ('collapse', ),
            'fields': ('large_img', 'medium_img', 'small_img'),
        }),
    )

@admin.register(AssetTransaction)
class AssetTransactionAdmin(admin.ModelAdmin):
    list_display = ('ts', 'user', 'asset', 'trans', 'note')
    # date_hierarchy = ['ts']
    # list_filter = ('trans')
    # ordering = ('ts',)

# admin.site.register(Asset)
#admin.site.register(AssetTransaction)
admin.site.register(Person)
admin.site.register(Genre)
