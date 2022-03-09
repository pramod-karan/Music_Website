from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(label="enter name", required = True)
    contact_email = forms.EmailField(label="enter email", required = True)
    content = forms.CharField(label="enter message", required = True, widget=forms.Textarea)