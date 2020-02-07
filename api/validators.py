from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .constants import TaskTypes

def validate_task_type(value):
    if value not in TaskTypes:
        raise ValidationError(
            _('%(value)s is not a task type'),
            params={'value': value},
        )