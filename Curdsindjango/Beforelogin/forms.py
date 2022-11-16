
from django import forms  

  
class RegistrationForm(forms.Form):
    name  = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    password = forms.CharField()

    # class Meta:
    #     model = Registration
    #     fields = "__all__"

    

# class Clean(forms.Form):
#     cleaned_data = self.clean()
#     cleaned_data = super().clean()
#     #super(RegistrationForm,self).clean()
#     name  = self.cleaned_data.get('name')
#     email = self.cleaned_data.get('email')
#     phone = self.cleaned_data.get('phone')
#     password = self.cleaned_data.get('passwod')
        

#         if len(name)<2:
#             raise forms.ValidationError('Name should be more than or equal 4')
#             #self.errors['name'] = self.error_class(['Enter Atleast 10 character'])

#         if len(email)<2:
#             raise forms.ValidationError('Enter Valid Email')
#             #self.errors['email'] = self.error_class(['Enter A Valid Email'])
        
#         if len(phone)<2:
#             raise forms.ValidationError('Name should be more than or equal 4')
#             #self.errors['phone'] = self.error_class(['Invalid Number'])
        
#         if len(password)<2:
#             raise forms.ValidationError('Name should be more than or equal 4')
#             #self.errors['password'] = self.error_class(['Incorrect Password'])



#         return super().clean()
        


# # from django.forms import ModelForm
# # from django import forms

# # from Beforelogin.models import User


# # class UserForm(ModelForm):

# #    # meta data for displaying a form
# #    class Meta:
# #       # model
# #       model = User

# #       # displaying fields
# #       fields = '__all__'

# #    # method for cleaning the data
# #    def clean(self):
# #       super(UserForm, self).clean()

# #       # getting username and password from cleaned_data
# #       username = self.cleaned_data.get('username')
# #       password = self.cleaned_data.get('password')

# #       # validating the username and password
# #       if len(username) < 5:
# #          self._errors['username'] = self.error_class(['A minimum of 5 characters is required'])

# #       if len(password) <= 8:
# #          self._errors['password'] = self.error_class(['Password length should not be less than 8 characters'])

# #       return self.cleaned_data