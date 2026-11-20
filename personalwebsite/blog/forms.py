from django import forms

class CommentForm(forms.Form):
    body = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Leave a comment!",
                "maxlength": 500,
            }
        )
    )
