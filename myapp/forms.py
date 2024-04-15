# forms.py
from django import forms

class CVUploadForm(forms.Form):
    cv_file = forms.FileField(label='Upload CV')
