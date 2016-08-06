#
#  Copyright (C) 2016 David Brookshire <dave@brookshire.org>
#
from django.contrib import admin
from .models import MovieAsset, AssetTransaction

# Register your models here.
admin.site.register(MovieAsset)
admin.site.register(AssetTransaction)