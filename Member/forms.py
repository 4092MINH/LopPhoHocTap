from django import forms
from .models import UpdatePlus
class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = UpdatePlus
        fields = ['ho', 'ten', 'student_id', 'additional_english_points', 'additional_literature_points', 'reason']  # Adjust fields as necessary