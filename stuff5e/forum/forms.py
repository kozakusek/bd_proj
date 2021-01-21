from django import forms
from .models import *
from django.contrib.auth.models import User
from chosen import forms as chosenforms

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
        
class SpellForm(forms.ModelForm):
    class Meta:
        model = Spell
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}), 
            'time': forms.Select(attrs={'class': 'form-control'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
            'range': forms.Select(attrs={'class': 'form-control'}),  
            'm': forms.TextInput(attrs={'class': 'form-control'}), 
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'classes': chosenforms.ChosenSelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usr_get', 'type':'hidden'}),
            'custom': forms.CheckboxInput(attrs={'class': 'form-control', 'value':'True', 'type':'hidden'})
        }
        
class FeatForm(forms.ModelForm):
    class Meta:
        model = Feat
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'prerequisite': forms.TextInput(attrs={'class': 'form-control'}),
            'bonuses': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usr_get', 'type':'hidden'}),
            'custom': forms.CheckboxInput(attrs={'class': 'form-control', 'value':'True', 'type':'hidden'})
        }
        
class RaceForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bonuses': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'speed': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usr_get', 'type':'hidden'}),
            'custom': forms.CheckboxInput(attrs={'class': 'form-control', 'value':'True', 'type':'hidden'})
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usr_get', 'type':'hidden'}),
            'custom': forms.CheckboxInput(attrs={'class': 'form-control', 'value':'True', 'type':'hidden'})
        }
        
class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = '__all__'
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usr_get', 'type':'hidden'}),
            'user_access': chosenforms.ChosenSelectMultiple(attrs={'class': 'form-control','value':'', 'id':'usr_get2'}),
        }
        
class JournalPostForm(forms.ModelForm):
    class Meta:
        model = JournalPost
        fields = ('title', 'body',)
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
 
class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),    
            'race': chosenforms.ChosenSelect(attrs={'class': 'form-control'}),   
            'starting_class': chosenforms.ChosenSelect(attrs={'class': 'form-control'}),    
            'story': forms.Textarea(attrs={'class': 'form-control'}),
            'feats': chosenforms.ChosenSelectMultiple(attrs={'class': 'form-control'}),
            'spells': chosenforms.ChosenSelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usr_get', 'type':'hidden'}),
            'user_access': chosenforms.ChosenSelectMultiple(attrs={'class': 'form-control'})
       }
        