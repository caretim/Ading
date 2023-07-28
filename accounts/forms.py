from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import NewUser



class UserSignup(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ["username"]



