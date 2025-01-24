from django import forms

class FirePredictionForm(forms.Form):
    latitude = forms.FloatField(label='Latitude')
    longitude = forms.FloatField(label='Longitude')
    brightness = forms.FloatField(label='Brightness')
    satellite = forms.FloatField(label='Satellite')
    frp = forms.FloatField(label='FRP')
    daynight = forms.FloatField(label='Day/Night')
    type_2 = forms.BooleanField(label='Type 2', required=False)
    type_3 = forms.BooleanField(label='Type 3', required=False)
    scan_binned = forms.FloatField(label='Scan Binned')
    year = forms.IntegerField(label='Year')
    month = forms.IntegerField(label='Month')
    day = forms.IntegerField(label='Day')
