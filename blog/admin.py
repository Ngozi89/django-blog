from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAmin(SummernoteModelAdmin):

    summernote_fields = ('content')
