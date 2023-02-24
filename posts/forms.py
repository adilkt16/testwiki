from django import forms
from posts.models import BlogPost
from django import template


register = template.Library()

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('name', 'slug', 'born', 'occupation' ,'education'  ,'insta_link', 'main_description' , 'career_description' , 'image',  )
        # exclude = ('is_accepted',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control input subheads', 'placeholder':'Name you want to display'}),
            'slug': forms.TextInput(attrs={'class':'form-control input', 'placeholder':'Copy the Name with no space and a hyphen in between'}),
            'occupation': forms.TextInput(attrs={'class':'form-control input ', 'placeholder':'Your Occupation'}),
            'education': forms.TextInput(attrs={'class':'form-control input ', 'placeholder':'Education status'}),
            'born': forms.TextInput(attrs={'class':'form-control input', 'placeholder':'EXAMPLE 28 April 1990 (age 32)'}),
            'insta_link': forms.TextInput(attrs={'class':'form-control input', 'placeholder':'example https://www.instagram.com/a_k_t_16/'}),
            'image': forms.FileInput(attrs={'class':'form-control  upload-button__icon input',}),
            'main_description': forms.Textarea(attrs={'class':'form-control input', 'placeholder':'Main Content of Yourself . Atleast 250 characters'}),
            'career_description': forms.Textarea(attrs={'class':'form-control input', 'placeholder':'Career Content of Yourself'}),
            
        }