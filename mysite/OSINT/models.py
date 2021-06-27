from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        """
        Creates and saves a User with the given email, nickname and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )
        print('ето пароль:', password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            nickname=nickname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    nickname = models.CharField(max_length=15)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', ]

    def __str__(self):

        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Requests(models.Model):
    RequestID = models.BigAutoField(primary_key=True)

    UserID = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING)

    URL = models.CharField(max_length=100, blank=False)
    DateCreate = models.DateField(auto_now=True)

    # Date = models.DateField(blank=True,null=True)
    Place = models.CharField(max_length=50, blank=True)
    FamilyInfo = models.CharField(max_length=50, blank=True)
    Interests = models.CharField(max_length=255, blank=True)
    Сharacter = models.CharField(max_length=255, blank=True)
    AddedPersonality = models.CharField(max_length=255, blank=True)
    GeoData = models.CharField(max_length=100, blank=True)
    Photos = models.ImageField(blank=True)
    Work = models.CharField(max_length=255, blank=True)
    AddedDInfo = models.CharField(max_length=255, blank=True)


class ResponsesByObject(models.Model):
    UniqueID = models.BigAutoField(primary_key=True)

    RequestID = models.ForeignKey(Requests, blank=False, on_delete=models.CASCADE)

    UserID = models.BigIntegerField(blank=False)

    URL = models.CharField(max_length=100, blank=False)

    Date = models.DateField(blank=True, null=True)
    Place = models.CharField(max_length=50, blank=True)
    FamilyInfo = models.CharField(max_length=50, blank=True)
    Interests = models.CharField(max_length=255, blank=True)
    Сharacter = models.CharField(max_length=255, blank=True)
    AddedPersonality = models.CharField(max_length=255, blank=True)
    GeoData = models.CharField(max_length=100, blank=True)
    Photos = models.ImageField(blank=True)
    Work = models.CharField(max_length=255, blank=True)
    AddedDInfo = models.CharField(max_length=255, blank=True)
# Create your models here.
