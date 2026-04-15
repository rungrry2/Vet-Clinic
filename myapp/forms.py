from django import forms
from .models import Owners as Owner, Pets as Pet, Appointments as Appointment


class OwnerForm(forms.ModelForm):

    class Meta:
        model = Owner
        fields = '__all__'
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone or phone.strip() == '':
            raise forms.ValidationError('เบอร์โทรศัพท์เป็นฟิลด์ที่จำเป็น กรุณาใส่เบอร์โทรศัพท์')
        
        # ลบเครื่องหมายขีดและช่องว่างเพื่อตรวจสอบความยาว
        cleaned_phone = str(phone).replace('-', '').replace(' ', '')
        
        if len(cleaned_phone) < 9:
            raise forms.ValidationError('เบอร์โทรศัพท์ต้องมีอย่างน้อย 9 หลัก')
        if len(cleaned_phone) > 10:
            raise forms.ValidationError('เบอร์โทรศัพท์ต้องไม่เกิน 10 หลัก')
        
        return phone
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # อีเมลไม่จำเป็น (สามารถเว้นได้)
        if email and email.strip():
            # ตรวจสอบรูปแบบอีเมล
            if '@' not in email or '.' not in email:
                raise forms.ValidationError('รูปแบบอีเมลไม่ถูกต้อง')
        return email or None


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight > 1000:
            raise forms.ValidationError('น้ำหนักต้องไม่เกิน 1000 กิโลกรัม')
        return weight


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'