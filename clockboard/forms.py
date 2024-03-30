from django import forms


class ResetClockForm(forms.Form):
    num_involved = forms.IntegerField(min_value=1, label='Number of people involved')
    comment = forms.CharField(required=False, widget=forms.Textarea)
