# Generated by Django 3.0.4 on 2020-03-08 06:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_type', models.CharField(blank=True, max_length=255)),
                ('previous_value', models.TextField(blank=True)),
                ('current_value', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ADD', 'ADD'), ('VIEW', 'VIEW'), ('CHANGE', 'CHANGE'), ('DELETE', 'DELETE')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserAuditLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('http_user_agent', models.CharField(blank=True, max_length=255, null=True)),
                ('remote_address', models.CharField(blank=True, max_length=255, null=True)),
                ('timezone', models.CharField(blank=True, max_length=255, null=True)),
                ('login_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('permissions', models.ManyToManyField(blank=True, related_name='permissions', to='authentication.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_group', to='authentication.UserGroups')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(blank=True, choices=[('CREATED', 'CREATED'), ('UPDATED', 'UPDATED'), ('DELETED', 'DELETED')], max_length=255, null=True)),
                ('activity_time', models.DateTimeField(auto_now_add=True)),
                ('user_email', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.CharField(blank=True, max_length=255)),
                ('value', models.ManyToManyField(blank=True, related_name='values', to='authentication.ActivityValue')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20)),
                ('firstname', models.CharField(blank=True, max_length=20)),
                ('lastname', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True)),
                ('last_password_updated', models.DateTimeField(blank=True, null=True)),
                ('user_contact_num', models.CharField(blank=True, max_length=255, null=True)),
                ('login_failure_counts', models.IntegerField(default=0)),
                ('activity_log', models.ManyToManyField(blank=True, related_name='activity_log', to='authentication.ActivityLog')),
                ('user_logs', models.ManyToManyField(blank=True, related_name='user_logs', to='authentication.UserAuditLogs')),
                ('user_roles', models.ManyToManyField(blank=True, related_name='user_roles', to='authentication.UserRoles')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
