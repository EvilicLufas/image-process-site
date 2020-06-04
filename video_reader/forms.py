from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class URLForm(forms.Form):
    video_url = forms.CharField(label='Video URL')

    def __init__(self, url=""):
        self.video_url = url
        super(URLForm, self).__init__()

    def is_valid(self):
        validate = URLValidator()
        try:
            validate(self.video_url)
            return True
        except ValidationError:
            return False
