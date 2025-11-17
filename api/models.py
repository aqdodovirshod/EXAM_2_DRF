from django.db import models
from accounts.models import CustomUser


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    schedule = models.CharField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="vacancy")


    def __str__(self):
        return f"{self.title} - {self.company}"


class Employee(models.Model):
    EMPLOYMENT_CHOICES = [
        ("full_time", "Full-time"),
        ("internship", "Internship"),
        ("part_time", "Part-time"),
        ("contract", "Contract work"),
        ("fifo", "FIFO"),
        ("volunteer", "Volunteering"),
    ]

    WORK_FORMAT_CHOICES = [
        ("hybrid", "Hybrid"),
        ("split", "Split"),
        ("on_site", "On-site"),
        ("remote", "Remote"),
    ]

    EXPERIENCE_CHOICES = [
        ("no_exp", "No experience"),
        ("1_3", "From 1 to 3 years"),
        ("3_6", "From 3 to 6 years"),
        ("6_plus", "More than 6 years"),
    ]

    EDUCATION_CHOICES = [
        ("bachelor", "Bachelor's degree"),
        ("master", "Master's degree"),
        ("phd", "PhD"),
        ("doctor", "Doctor of Sciences"),
        ("higher", "Higher education"),
        ("incomplete_higher", "Incomplete higher education"),
        ("secondary", "Secondary education"),
        ("vocational", "Vocational education"),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    employee_experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES, null=True, blank=True)
    level_of_education = models.CharField(max_length=20, choices=EDUCATION_CHOICES, null=True, blank=True)
    employment = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES, null=True, blank=True)
    work_format = models.CharField(max_length=10, choices=WORK_FORMAT_CHOICES, null=True, blank=True)


    def __str__(self):
        return f"{self.user.username} - {self.position}"
