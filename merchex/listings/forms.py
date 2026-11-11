from django import forms
from listings.models import Band,Listing

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
   class Meta: #Plus besoin de recopier chaque ligne du model, on peut tout importer directement
      model = Band
      fields = '__all__'
      #exclude = ('active', 'official_homepage') enlève c'est 2  champs

class ListingForm(forms.ModelForm):
   class Meta: #Plus besoin de recopier chaque ligne du model, on peut tout importer directement
      model = Listing
      fields = '__all__'
      #exclude = ('active', 'official_homepage') enlève c'est 2  champs