from django import forms

from .models import Category, Post


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, required=True, strip=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
#     text = forms.CharField(required=True, widget=forms.Textarea)
#     image = forms.ImageField()

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'text', 'image', 'user')


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'text', 'image')
