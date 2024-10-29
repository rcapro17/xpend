import uuid
from django.db import models

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)  # Added photo field

    def __str__(self):
        return self.name  # Display user's name

class Household(models.Model):
    household_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    household_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="households", null=True)  # Allow multiple users in a household
    photo = models.ImageField(upload_to='household_photos/', blank=True, null=True)  # Added photo field

    def __str__(self):
        return self.household_name  # Display household name

class IncomeType(models.Model):
    incomeType_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    incomeType_name = models.CharField(max_length=255)

    def __str__(self):
        return self.incomeType_name  # Display income type name


class IncomeSource(models.Model):
    incomeSource_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    incomeSource_name = models.CharField(max_length=255)

    def __str__(self):
        return self.incomeSource_name  # Display income source name

class Income(models.Model):
    income_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    income_name = models.CharField(max_length=255)
    income_amount_gross = models.DecimalField(max_digits=10, decimal_places=2)
    income_amount_net = models.DecimalField(max_digits=10, decimal_places=2)
    income_date = models.DateField()
    income_type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    income_source = models.ForeignKey(IncomeSource, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes", null=True)  # Link income to a user

    def __str__(self):
        return self.income_name  # Display income name

class ExpenseType(models.Model):
    expenseType_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    expenseType_name = models.CharField(max_length=255)

    def __str__(self):
        return self.expenseType_name  # Display expense type name

class ExpenseCategory(models.Model):
    expenseCategory_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    expenseCategory_name = models.CharField(max_length=255)

    def __str__(self):
        return self.expenseCategory_name  # Display expense category name

class ExpenseName(models.Model):  # Define the ExpenseName model
    expense_name_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  # Display expense name

class Expense(models.Model):
    expense_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    expense_date = models.DateField()
    expense_name = models.ForeignKey(ExpenseName, on_delete=models.CASCADE)  # Ensure this references the new model
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)  # Include receipt field
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses", null=True)


    def __str__(self):
        return f"{self.expense_name} on {self.expense_date}"  # Display expense name and date
