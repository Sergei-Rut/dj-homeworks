from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                count += 1
            if count == 0:
                raise ValidationError('Должен быть хотя бы один основной тэг')
            if count > 1:
                raise ValidationError('Должен быть всего один основной тэг')
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 0
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    list_filter = ['published_at']
    inlines = [ArticleTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ArticleTagInline]
