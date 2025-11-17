from django.urls import path
from .views import VacancyListCreateView, VacancyRetriveUpdateDeleteView, EmployeeListCreateView, EmployeeRetrieveUpdateDeleteView

urlpatterns = [
    path("vacancy/", VacancyListCreateView.as_view()),
    path("vacancy/<int:pk>/", VacancyRetriveUpdateDeleteView.as_view()),
    path('employee/', EmployeeListCreateView.as_view()),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateDeleteView.as_view())
]