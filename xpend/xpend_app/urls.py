
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    HouseholdViewSet,
    IncomeViewSet,
    IncomeTypeViewSet,
    IncomeSourceViewSet,
    ExpenseViewSet, # Include this if you have an ExpenseViewSet
    ExpenseCategoryViewSet, # Include this if you have an ExpenseSourceViewSet
    ExpenseTypeViewSet # Include this if you have an ExpenseTypeView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'households', HouseholdViewSet)
router.register(r'incomes', IncomeViewSet)
router.register(r'income-types', IncomeTypeViewSet)
router.register(r'income-sources', IncomeSourceViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'expenses-type', ExpenseTypeViewSet)  # Register ExpenseViewSet
router.register(r'expenses-category', ExpenseCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
