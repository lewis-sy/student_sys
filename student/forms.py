from django.forms import forms

from .models import Student


class StudentForm(forms.Form):
    def clean_qq(self):
        cleaned_data = self.clean_data['qq']
        if not cleaned_data.isdigit():
            raise  forms.ValidationError('必须是数字!')

        return int(cleaned_data)

    class Meta:
        model = Student
        Fields = {
            'name','sex','profession',
            'email','qq','phone',
        }