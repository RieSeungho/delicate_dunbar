from django import forms
from posts.models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'post',
            'content',
        ]
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': '댓글을 입력해주세요...',
            })
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'content',
        ]