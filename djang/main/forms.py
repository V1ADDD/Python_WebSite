from .models import Ask
from django.forms import ModelForm, TextInput, Textarea

class AskForm(ModelForm):
    class Meta:
        model = Ask
        fields = ["gmail", "question"]
        widgets = {
            "gmail": TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Ваша почта...'
            }),
            "question": Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Ваше сообщение...'
            }),
        }
