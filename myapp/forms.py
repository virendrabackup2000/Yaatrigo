from .models import Bus, Train
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,

)
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
        
class AddTrainForm(forms.ModelForm):
    train_no = forms.IntegerField(label='Train no.')
    train_name = forms.CharField(label='Train Name.')
    source = forms.CharField(label='Source')
    dest = forms.CharField(label='Destination')
    total_km = forms.DecimalField(label='Total KM')
    travel_time = forms.DecimalField(label='travel_time')
    nos = forms.DecimalField(label='no. of seats')
    price = forms.DecimalField(label='Price')
    date = forms.DateField()
    time = forms.TimeField()
    class Meta:
        model = Train
        fields = [
            'train_no','train_name','source',
            'dest','total_km','travel_time','nos','price','date','time'
        ]

      
class AddBusForm(forms.ModelForm):
    bus_no = forms.IntegerField(label='Bus no.')
    bus_name = forms.CharField(label='Bus Name.')
    source = forms.CharField(label='Source')
    dest = forms.CharField(label='Destination')
    total_km = forms.DecimalField(label='Total KM')
    travel_time = forms.DecimalField(label='travel_time')
    nos = forms.DecimalField(label='no. of seats')
    price = forms.DecimalField(label='Price')
    date = forms.DateField()
    time = forms.TimeField()
    class Meta:
        model = Bus
        fields = [
            'bus_no','bus_name','source',
            'dest','total_km','travel_time','nos','price','date','time'
        ]
