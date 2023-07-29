from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email field must be valid")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Languages(models.Model):
    prefix = models.CharField(max_length=2)
    name = models.CharField(max_length=100)


class EmployerUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=32, null=True, blank=True)
    surname = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='employer_users',
        related_query_name='employer_user',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='employer_users',
        related_query_name='employer_user',
        blank=True,
    )
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name', 'website']


class JobSeekerUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=32, null=True, blank=True)
    surname = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(unique=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    language_known = models.ForeignKey(Languages, on_delete=models.CASCADE, blank=True, null=True)
    github_profile = models.URLField(max_length=200, blank=True, null=True)
    codewars_profile = models.URLField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='job_seeker_users',
        related_query_name='job_seeker_user',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='job_seeker_users',
        related_query_name='job_seeker_user',
        blank=True,
    )
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['surname']


class JobListing(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    required_language = models.ForeignKey(Languages, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField()
    employer = models.ForeignKey('EmployerUser', related_name='job_listings', on_delete=models.CASCADE)


class WorkExperience(models.Model):
    experience_of_job_seeker = models.ForeignKey(JobSeekerUser, related_name='work_experiences', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    job_description = models.TextField()


class Education(models.Model):
    education_of_job_seeker = models.ForeignKey(JobSeekerUser, related_name='educations', on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField()


class Skill(models.Model):
    skill_of_job_seeker = models.ForeignKey(JobSeekerUser, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Endorsement(models.Model):
    endorsement_of_job_seeker = models.ForeignKey(JobSeekerUser, related_name='endorsements_received', on_delete=models.CASCADE)
    endorsed_by = models.ForeignKey(JobSeekerUser, related_name='endorsements_given', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class Recommendation(models.Model):
    recommendation_of_job_seeker = models.ForeignKey(JobSeekerUser, related_name='received_recommendations', on_delete=models.CASCADE)
    given_by = models.ForeignKey(EmployerUser, related_name='given_recommendations', on_delete=models.CASCADE)
    content = models.TextField()


class Certification(models.Model):
    certification_of_job_seeker = models.ForeignKey(JobSeekerUser, related_name='certifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)


class JobApplication(models.Model):
    job_seekers = models.ManyToManyField(JobSeekerUser, related_name='job_applications')
    job_listing = models.ForeignKey(JobListing, related_name='applications', on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['job_listing', 'application_date']
