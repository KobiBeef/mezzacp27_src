from . import models
from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

# Register your models here.
author_extra_fieldsets = ((None, {"fields": ("dob",)}),)

class BookInLine(admin.TabularInline):
	model = models.Book

class TestAssistsInLine(admin.TabularInline):
	model = models.TestAssist

class AuthorAdmin(PageAdmin):
	inlines = (BookInLine,)
	fieldsets = deepcopy(PageAdmin.fieldsets) + author_extra_fieldsets

class ProgrammingAdmin(PageAdmin):
	inlines = (TestAssistsInLine,)

class TestModelAdmin(admin.ModelAdmin):
	list_display = ("title",)

admin.site.register(models.DocPage, PageAdmin)
admin.site.register(models.Programming, ProgrammingAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.TestModel, TestModelAdmin)