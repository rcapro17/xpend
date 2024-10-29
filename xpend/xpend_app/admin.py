from django.contrib import admin
from .models import User, Household, Income, IncomeType, IncomeSource, Expense, ExpenseType, ExpenseCategory

# Register your models here
admin.site.register(User)
admin.site.register(Household)
admin.site.register(Income)
admin.site.register(IncomeType)
admin.site.register(IncomeSource)
admin.site.register(Expense)
admin.site.register(ExpenseType)
admin.site.register(ExpenseCategory)
