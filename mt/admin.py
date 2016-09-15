#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
from django.contrib import admin
from .models import Asset, AssetTransaction, Person, Genre

# Register your models here.
admin.site.register(Asset)
admin.site.register(AssetTransaction)
admin.site.register(Person)
admin.site.register(Genre)