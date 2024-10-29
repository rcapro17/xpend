from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User, Household, Income, IncomeType, IncomeSource, Expense, ExpenseType, ExpenseCategory
from .serializers import (
    UserSerializer,
    HouseholdSerializer,
    IncomeSerializer,
    IncomeTypeSerializer,
    IncomeSourceSerializer,
    ExpenseTypeSerializer,
    ExpenseCategorySerializer,
    ExpenseSerializer  # Import the ExpenseSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Save the user with the uploaded photo if provided
        serializer.save()

class HouseholdViewSet(viewsets.ModelViewSet):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializer

    def perform_create(self, serializer):
        # Save the household with the uploaded photo if provided
        serializer.save()

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def perform_create(self, serializer):
        # Optionally, you could add logic here if needed
        serializer.save()

class IncomeTypeViewSet(viewsets.ModelViewSet):
    queryset = IncomeType.objects.all()
    serializer_class = IncomeTypeSerializer

# class IncomeCategoryViewSet(viewsets.ModelViewSet):
#     queryset = IncomeCategory.objects.all()
#     serializer_class = IncomeCategorySerializer

class IncomeSourceViewSet(viewsets.ModelViewSet):
    queryset = IncomeSource.objects.all()
    serializer_class = IncomeSourceSerializer

class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class ExpenseTypeViewSet(viewsets.ModelViewSet):
    queryset = ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer

# class ExpenseType(models.Model):
#     expenseType_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     expenseType_name = models.CharField(max_length=255)

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        # Save the expense with the uploaded receipt if provided
        serializer.save()
