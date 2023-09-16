from django import forms
from .models import Comment

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'stars')
