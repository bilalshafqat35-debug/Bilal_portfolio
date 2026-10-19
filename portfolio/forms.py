from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Your Message', 'rows': 4}),
        }