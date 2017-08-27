from django import forms

from .validators import validate_dot_com,validate_Url


class verifyForm (forms.Form):
    url=forms.CharField(label=' ',validators=[validate_dot_com,validate_Url])


#    def clean_url(self):
    #    url=self.cleaned_data['url']
     #   url_validator=URLValidator()
      #  try:
       #     url_validator(url)
        #except:
         #   raise forms.ValidationError("Invalid Url For This Field")

#        return url
