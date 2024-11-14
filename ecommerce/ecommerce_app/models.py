from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from wtforms.fields import EmailField


class Permission(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    permissions = models.ManyToManyField("Permission", through="RolePermission", related_name="roles")

    def __str__(self):
        return self.name

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True, null=True)
    email = EmailField(unique=True)
    address = models.CharField(max_length=255, null=True)
    avatar = CloudinaryField('avatar', null=True)
    roles = models.ManyToManyField("Role", through="UserRole",related_name="users")

    def __str__(self):
        return self.username + " " + self.email

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)