from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField()
    mail = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def send_email(self):
        # send email using the self.cleaned_data dictionary
        s = send_mail(
            'Message from Nucapacha.com',
            self.cleaned_data['message'],
            self.cleaned_data['mail'],
            ['contact@nucapacha.com'],
            fail_silently=False,
        )
