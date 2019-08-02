from django import forms


class GameCodeForm(forms.Form):
    code = forms.CharField(max_length=4)
    name = forms.CharField(max_length=12)

    def clean(self):
        cleaned_data = super(GameCodeForm, self).clean()
        code = cleaned_data.get("code")
        name = cleaned_data.get("name")
        if not code or not name:
            raise forms.ValidationError("Uh, you need a game code and name...")
