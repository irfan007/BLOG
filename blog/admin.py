from django.contrib import admin
from blog.models import Tag, Post, Comment
from django.forms import *
from django.db.models import *
from tinymce.widgets import TinyMCE

class TagAdmin(admin.ModelAdmin):
	pass


class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_date'
	list_display = ('title', 'pub_date', 'last_modified','allow_comment')
	search_fields = ('title', 'body')
	list_filter = ('pub_date',)
	prepopulated_fields = {'slug': ('title',)}
	ordering = ('-pub_date',)
	filter_horizontal = ('tags',)


class CommentAdmin(admin.ModelAdmin):
	pass




admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
