# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppointmentStatus(models.Model):
    status_id = models.CharField(primary_key=True, max_length=6)
    status_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Appointment_Status'


class Appointments(models.Model):
    appointment_id = models.CharField(primary_key=True, max_length=6)
    pet = models.ForeignKey('Pets', models.DO_NOTHING)
    vet = models.ForeignKey('Veterinarians', models.DO_NOTHING)
    status = models.ForeignKey(AppointmentStatus, models.DO_NOTHING)
    appointment_date = models.DateField(blank=True, null=True)
    appointment_time = models.TimeField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Appointments'


class Bills(models.Model):
    bill_id = models.CharField(primary_key=True, max_length=6)
    record = models.ForeignKey('MedicalRecords', models.DO_NOTHING)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, blank=True, null=True)
    bill_date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bills'


class MedicalRecords(models.Model):
    record_id = models.CharField(primary_key=True, max_length=6)
    pet = models.ForeignKey('Pets', models.DO_NOTHING)
    vet = models.ForeignKey('Veterinarians', models.DO_NOTHING, blank=True, null=True)
    visit_date = models.DateField(blank=True, null=True)
    symptoms = models.TextField(db_collation='Thai_CI_AS', blank=True, null=True)
    diagnosis = models.TextField(db_collation='Thai_CI_AS', blank=True, null=True)
    treatment = models.TextField(db_collation='Thai_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Medical_Records'


class MedicineStock(models.Model):
    stock_id = models.CharField(primary_key=True, max_length=6)
    medicine = models.ForeignKey('Medicines', models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Medicine_Stock'


class Medicines(models.Model):
    medicine_id = models.CharField(primary_key=True, max_length=6)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    medicine_name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Medicines'


class Owners(models.Model):
    owner_id = models.CharField(primary_key=True, max_length=6)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Owners'


class PaymentMethod(models.Model):
    payment_method_id = models.CharField(primary_key=True, max_length=6)
    method_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Payment_Method'


class PetAllergies(models.Model):
    allergy_id = models.CharField(primary_key=True, max_length=6)
    pet = models.ForeignKey('Pets', models.DO_NOTHING)
    allergy_detail = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pet_Allergies'


class Pets(models.Model):
    pet_id = models.CharField(primary_key=True, max_length=6)
    owner = models.ForeignKey(Owners, models.DO_NOTHING)
    species = models.ForeignKey('Species', models.DO_NOTHING)
    pet_name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pets'


class Species(models.Model):
    species_id = models.CharField(primary_key=True, max_length=6)
    species_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Species'


class Staff(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=6)
    staff_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Staff'


class Suppliers(models.Model):
    supplier_id = models.CharField(primary_key=True, max_length=6)
    supplier_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Suppliers'


class Treatments(models.Model):
    treatment_id = models.CharField(primary_key=True, max_length=6)
    record = models.ForeignKey(MedicalRecords, models.DO_NOTHING)
    medicine = models.ForeignKey(Medicines, models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    instruction = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Treatments'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=6)
    staff = models.ForeignKey(Staff, models.DO_NOTHING)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'


class Vaccinations(models.Model):
    vaccination_id = models.CharField(primary_key=True, max_length=6)
    pet = models.ForeignKey(Pets, models.DO_NOTHING)
    vaccine_name = models.CharField(max_length=100, blank=True, null=True)
    vaccination_date = models.DateField(blank=True, null=True)
    next_due_date = models.DateField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vaccinations'


class Veterinarians(models.Model):
    vet_id = models.CharField(primary_key=True, max_length=6)
    vet_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Veterinarians'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
