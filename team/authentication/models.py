from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone


# Model Managers will start from here
class CustomUserManager(BaseUserManager):

    def create_user(self, kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        user = self.model(
            email=self.normalize_email(kwargs['email']),
            #            username=kwargs['username'],
        )

        user.set_password(kwargs['password'])
        user.firstname = kwargs['firstname']
        user.lastname = kwargs['lastname']
        user.save(self._db)
        user.last_password_updated = user.date_joined

        user.save()

        return user

    def update_user(self, kwargs):
        """
        Functions used to update User details
        :param kwargs:
        :return:
        """
        user = self.get_user_by_email(kwargs['email'])
        user.firstname = kwargs['firstname']
        user.lastname = kwargs['lastname']
        #         user.email = kwargs['new_email']
        user.save()

    def users(self):
        """
        Function returns all the users
        :return:
        """
        return self.all()


# Create your models here.
class Permission(models.Model):
    """
    The Permission model will assign permissions to users and Groups
    The following Permissions will be defined:
    1. Add
    2. View
    3. Change
    4. Delete
    """
    PERMISSIONS = (
        ("ADD", "ADD"),
        ("VIEW", "VIEW"),
        ("CHANGE", "CHANGE"),
        ("DELETE", "DELETE")
    )

    name = models.CharField(max_length=255, choices=PERMISSIONS)


class UserGroups(models.Model):
    """
    Groups will be a generic way of categorizing users to apply
    permissions. A user can belong to any number of groups
    The following groups will be there:
    1. USER_ADMIN
    2. APP_ADMIN
    3. EoX Viewer

    """

    name = models.CharField(max_length=150, unique=True, blank=True)
    permissions = models.ManyToManyField(Permission,
                                         related_name='permissions',
                                         blank=True
                                         )

class UserRoles(models.Model):
    group = models.ForeignKey(UserGroups, related_name='role_group', on_delete=models.CASCADE)

class ActivityValue(models.Model):
    value_type = models.CharField(max_length=255, blank=True)
    previous_value = models.TextField(blank=True)
    current_value = models.TextField(blank=True)


class ActivityLog(models.Model):
    ACTIVITY = (
        ('CREATED', 'CREATED'),
        ('UPDATED', 'UPDATED'),
        ('DELETED', 'DELETED')
    )
    activity = models.CharField(max_length=255, blank=True, null=True, choices=ACTIVITY)
    activity_time = models.DateTimeField(auto_now_add=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True)
    value = models.ManyToManyField(ActivityValue, related_name='values', blank=True)


class UserAuditLogs(models.Model):
    """
    Model will be used to track the User login
    activities like IPAddress,Browser,Timezone,login time,
    OS
    """
    http_user_agent = models.CharField(max_length=255, blank=True, null=True)
    remote_address = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    login_time = models.DateTimeField(auto_now=True)


class CustomUser(AbstractBaseUser):  # Custom User Model to use email as user identifier instead of username
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20, blank=True)
    lastname = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True, unique=True)

    objects = CustomUserManager()
    """Django user model related fields"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    is_active = models.BooleanField(default=True)
    last_password_updated = models.DateTimeField(blank=True, null=True)
    user_contact_num = models.CharField(max_length=255, blank=True, null=True)
    user_roles = models.ManyToManyField(UserRoles, related_name='user_roles',blank=True)
    user_logs = models.ManyToManyField(UserAuditLogs, related_name='user_logs',blank=True)
    login_failure_counts = models.IntegerField(default=0)
    activity_log = models.ManyToManyField(ActivityLog, related_name='activity_log', blank=True)


