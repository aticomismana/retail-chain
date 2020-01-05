from django.contrib import admin
from .models import BankAccount, NaturalPerson, Store, StoreBranch, Supplier

# Register your models here.

admin.site.register(BankAccount)
admin.site.register(NaturalPerson)
admin.site.register(Store)
admin.site.register(StoreBranch)
admin.site.register(Supplier)
