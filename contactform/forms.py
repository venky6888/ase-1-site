from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20,required = True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class ReplyForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    reply_message = forms.CharField(widget = forms.Textarea, max_length = 150,required = True)