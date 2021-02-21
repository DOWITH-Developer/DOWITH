from django import forms
from .models import Challenge


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = "__all__"

    # def clean_max_pp(self):
    #     max_pp = self.cleaned_data.get("max_pp")
    #     min_pp = self.cleaned_data.get('min_pp')
    #     if max_pp < min_pp:
    #         raise forms.ValidationError("더 작음")
    #     return max_pp

class SearchForm(forms.Form):
    search_word = forms.CharField(label = "")