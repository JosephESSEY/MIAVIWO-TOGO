from blog.models import Article
from django.contrib import admin
from . import models
from blog.models import *


@admin.register(Article)
class Article(admin.ModelAdmin):
    model = Article

    list_display = (
        "id",
        "title",
        "slug",
        "publish_date",
        "is_draft",
    )
    list_filter = (
        "is_draft",
        "publish_date",
    )
    list_editable = (
        "title",
        "slug",
        "is_draft",
    )
    search_fields = (
        "title",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            )
    }
    date_hierarchy = "publish_date"
    save_on_top = True


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    model = Categorie


@admin.register(HitCount)
class HitCountAdmin(admin.ModelAdmin):
    model = HitCount






