from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Название занято')
        return new_slug
        if Tag.objacts.filter(slug__iexact=new_slug).count():
            raise ValidationError('Этот слаг неправильно заполнен')
        return new_slug

    def save(self):
        new_tag = Tag.objects.create(
            title=self.cleaned_data['title'],
            slug=self.cleaned_data['slug'],
        )
        return new_tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Название занято')
        return new_slug
        if Post.objacts.filter(slug__iexact=new_slug).count():
            raise ValidationError('Этот слаг неправильно заполнен')
        return new_slug

    def save(self):
        new_post = Post.objects.create(
            title=self.cleaned_data['title'],
            slug=self.cleaned_data['slug'],
        )
        return new_post
