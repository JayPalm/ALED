from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):
	class Meta:
		model = Signup
		exclude = ['trip','date','submitter','car','car_auto_added']
		yesno = ((0,"No"),(1,"Yes"))
		has_car = forms.ChoiceField(choices=yesno, widget=forms.RadioSelect)
		#car = forms.ChoiceField(widget=forms.RadioSelect)
