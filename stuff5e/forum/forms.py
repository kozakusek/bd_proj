from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usr_get', 'type':'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body',)
        
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usr_get', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }