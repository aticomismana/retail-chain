from django.db import models

# Create your models here.

class BankAccount(models.Model):
    bank_account_id = models.AutoField(primary_key=True)
    bank = models.IntegerField('Bank')
    bank_branch = models.IntegerField('Bank Branch')
    number = models.CharField('Number', max_length=20)

    def __str__(self):
        return self.number

    class Meta:
        unique_together = ('bank', 'bank_branch', 'number',)

class Person(models.Model):
    name = models.CharField('Name', max_length=60)
    address = models.CharField('Address', max_length=255)
    phone_number = models.CharField('Phone Number', max_length=20)
    bank_account = models.OneToOneField(BankAccount, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class NaturalPerson(Person):
    natural_person_id = models.AutoField(primary_key=True)
    identification_number = models.CharField('Identification Number', max_length=20, unique=True)

class LegalPerson(Person):
    registered_number = models.CharField('Registered Number', max_length=20, unique=True)
    representatives = models.ManyToManyField(NaturalPerson)

    class Meta:
        abstract = True

class Store(LegalPerson):
    store_id = models.AutoField(primary_key=True)

class StoreBranch(LegalPerson):
    store_branch_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='branches',
        related_query_name="branch"
    )
    suppliers = models.ManyToManyField('Supplier')

class Supplier(LegalPerson):
    supplier_id = models.AutoField(primary_key=True)
