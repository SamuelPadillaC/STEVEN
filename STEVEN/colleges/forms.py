from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    nationality = forms.CharField()
    major = forms.CharField()
    language = forms.ChoiceField(choices=[('english', 'English'), ('spanish', 'Spanish'), ('portuges','Portuges'), ('german', 'German'), ('chinese','Chinese'), ('japanese','Japanese')])
    email = forms.EmailField(label = 'E-mail')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput) 