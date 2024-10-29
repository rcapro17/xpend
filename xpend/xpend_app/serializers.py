from rest_framework import serializers
from .models import User, Household, Income, IncomeType, IncomeSource, Expense, ExpenseType, ExpenseCategory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'email', 'telephone', 'photo']  # Include the photo field

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = ['household_id', 'household_name', 'user', 'photo']  # Include the photo field

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['income_id', 'income_name', 'income_amount_gross', 'income_amount_net', 'income_date', 'income_type', 'income_source', 'user']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['expense_id', 'expense_date', 'expense_name', 'expense_category', 'expense_type', 'receipt']  # Include the receipt field


class IncomeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeType
        fields = ['incomeType_id', 'incomeType_name']  # Adjust based on your model fields


class IncomeSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeSource
        fields = ['incomeSource_id', 'incomeSource_name']

class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseType
        fields = ['expensesType_id', 'expensesType_name']

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['expensesCategory_id', 'expensesCategory_name']
                 

                