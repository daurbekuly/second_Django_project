from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announce', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'

            }),
            "announce": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'

            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'гггг-мм-дд чч.мм.сс',
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'

            }),
        }