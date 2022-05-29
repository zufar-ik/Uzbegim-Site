from django import forms

from .models import Registration


class Reg(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['rooms','first_name','last_name','admin','pasport_serial_num','birth_date','img','guest_count','room_bool']
        widgets = {
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }

class Update(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['leave_date']
        widgets = {
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }