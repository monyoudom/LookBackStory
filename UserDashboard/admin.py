
# Register your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile,Book,Page,UserBook,UserBookPage,PageContent,PageContentUser


admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Page)
admin.site.register(UserBook)
admin.site.register(UserBookPage)
admin.site.register(PageContent)
admin.site.register(PageContentUser)


