from django import forms
from FApp.models import FamilyMember,Profile
from django.forms.models import inlineformset_factory

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        exclude = ()
FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember,form=FamilyMemberForm, extra=1)
