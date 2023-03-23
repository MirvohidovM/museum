from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """Manager for User profiles"""

    def create_user(self, *args, **kwargs):

        user = self.model(*args, **kwargs)
        return super(CustomUser).save(user)

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class CustomUser(AbstractUser):
    ADMIN = 1
    MODERATOR = 2
    INTERN = 3

    ROLE_CHOICE = (
        (ADMIN, 'Admin'),
        (MODERATOR, 'Moderator'),
        (INTERN, 'Intern'),
    )

    username = models.CharField(max_length=255, unique=True)
    firstname = models.CharField(max_length=100, verbose_name="Исм")
    lastname = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICE, null=True, blank=True)

    # USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    class Meta:

        verbose_name = "Фойдаланувчи"
        verbose_name_plural = "Фойдаланувчилар"

    def __str__(self):
        return self.firstname + self.lastname
