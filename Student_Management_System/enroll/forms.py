from django import forms
from .models import Stundent


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Stundent
        fields = '__all__'
        widgets={'Fname': forms.TextInput(attrs={'class': 'input--style-5', 'maxlength': '150', 'required': 'true'}),
            'Lname': forms.TextInput(attrs={'class': 'input--style-5', 'maxlength': '150', 'required': 'true'}),
            'username': forms.TextInput(attrs={'class': 'input--style-5', 'maxlength': '150', 'required': 'true'}),
            'password': forms.PasswordInput(attrs={'class': 'input--style-5', 'maxlength': '150', 'required': 'true'}),
            'branch': forms.TextInput(attrs={'class': 'input--style-5', 'maxlength': '150', 'required': 'true'}),
            'rollno': forms.TextInput(attrs={'class': 'input--style-5', 'maxlength': '150', 'required': 'true'}),
            'contactno': forms.TextInput(attrs={'class': 'input--style-5', 'maxlength': '150', 'required': 'true'}),
        }
        labels = {
            'Fname': 'First Name',
            'Lname': 'Last Name',
            'username': 'Username',
            'password': 'Password',
            'branch': 'Branch',
            'rollno': 'Roll No',
            'contactno': 'Contact No',
        }
class Student_login(forms.ModelForm):
    class Meta:
        model=Stundent
        fields=['username','password']
        widgets={ 'username': forms.TextInput(attrs={'class': 'input--style-5', 'maxlength': '150', 'required': 'true'}),
            'password': forms.PasswordInput(attrs={'class': 'input--style-5', 'maxlength': '150', 'required': 'true'}),}
        