# Generated by Django 4.0.6 on 2022-07-10 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('port', models.SmallIntegerField()),
                ('resource_type', models.CharField(choices=[('Windows', 'Windows'), ('Unix', 'Unix'), ('SQL', 'SQL')], default=None, max_length=150)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('host_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]