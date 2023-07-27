from django.contrib.auth.models import AbstractUser
from django.db import models


class Languages(models.Model):
    prefix = models.CharField(max_length=2)
    name = models.CharField(max_length=100)

class TechStack(models.Model):
    name = models.CharField(max_length=100)

class JobListing(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    required_language = models.ForeignKey(Languages, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField()
    employer = models.ForeignKey('EmployerUser', related_name='job_listings', on_delete=models.CASCADE)

class EmployerUser(AbstractUser):
    company_name = models.CharField(max_length=100)
    website = models.CharField(max_length=200)

class JobSeekerUser(AbstractUser):
    cv = models.FileField()
    location = models.CharField(max_length=100)
    language = models.ForeignKey(Languages, related_name='job_seekers', on_delete=models.CASCADE)
    tech_stack = models.ManyToManyField(TechStack, related_name='job_seekers', blank=True)
    github_profile = models.URLField(max_length=200, blank=True, null=True)
    codewars_profile = models.URLField(max_length=200, blank=True, null=True)

class WorkExperience(models.Model):
    job_seeker = models.ForeignKey(JobSeekerUser, related_name='work_experiences', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    job_description = models.TextField()

class Education(models.Model):
    job_seeker = models.ForeignKey(JobSeekerUser, related_name='educations', on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField()

class Skill(models.Model):
    job_seeker = models.ForeignKey(JobSeekerUser, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Endorsement(models.Model):
    job_seeker = models.ForeignKey(JobSeekerUser, related_name='endorsements_received', on_delete=models.CASCADE)
    endorsed_by = models.ForeignKey(JobSeekerUser, related_name='endorsements_given', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

class Recommendation(models.Model):
    job_seeker = models.ForeignKey(JobSeekerUser, related_name='received_recommendations', on_delete=models.CASCADE)
    given_by = models.ForeignKey(EmployerUser, related_name='given_recommendations', on_delete=models.CASCADE)
    content = models.TextField()

class Certification(models.Model):
    job_seeker = models.ForeignKey(JobSeekerUser, related_name='certifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)

class JobApplication(models.Model):
    job_seeker = models.ForeignKey(JobSeekerUser, related_name='job_applications', on_delete=models.CASCADE)
    job_listing = models.ForeignKey(JobListing, related_name='applications', on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
