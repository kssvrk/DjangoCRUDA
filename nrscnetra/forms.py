from django import forms
  
# import GeeksModel from models.py
from nrscnetra.models import System
  
# create a ModelForm
class SystemForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = System
        fields = ['title','ip_address']