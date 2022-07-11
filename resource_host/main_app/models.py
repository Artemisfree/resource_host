from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

User = get_user_model()


class Host(models.Model):
    TYPE = (
        ('Windows', 'Windows'),
        ('Unix', 'Unix'),
        ('SQL', 'SQL'),
    )
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    port = models.SmallIntegerField()
    resource_type = models.CharField(
        max_length=150,
        choices=TYPE,
        default=None
    )
    host_owner = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='hosts'
    )
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=False)
