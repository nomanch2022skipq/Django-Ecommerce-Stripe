from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Order


@receiver(pre_delete, sender=Order)
def prevent_deletion(sender, instance, **kwargs):
    raise ValidationError("This field cannot be deleted.")
