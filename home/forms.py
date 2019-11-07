from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category', 'draft']

    def clean_title(self):
        title = self.cleaned_data['title']

        if title.isdigit():
            raise forms.ValidationError('Lütfen Yalnızca Sayı Girişi Yapmayınız.')

        return title
