from django.db import models

class MemberManager(models.Manager):
    def get_all_member_details(self):
        return self.values('member_id', 'first_name', 'last_name', 'email', 'phone', 'member_type', 'created_at')

    def get_all_members(self):
        return self.all()

    def get_team_member(self, member_id):
        return self.filter(member_id=member_id).values()

    def add_team_member(self, **data):
        member_obj, created = self.get_or_create(**data)
        return member_obj

    def edit_team_member(self, **data):
        member_id = data.get('member_id')
        member_obj = self.filter(member_id=member_id)
        if member_obj:
            member_obj.update(**data)
            return member_obj[0]
        else:
            return "Object Not Found"

    def delete_team_member(self, member_id):
        member_obj = self.get(member_id=member_id)
        member_obj.delete()
        return member_obj

class Member(models.Model):
    """
    This model describes a team-member object and data pertaining to it.
    """
    TYPE = (
        ('ADMIN', 'ADMIN'),
        ('REGULAR', 'REGULAR'),
    )

    member_id = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    member_type = models.CharField(max_length=100, choices=TYPE, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    manager = MemberManager()

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name