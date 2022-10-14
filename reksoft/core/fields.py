from django.db import models
from django_case_insensitive_field import (
    CaseInsensitiveFieldMixin as LowerCaseCaseInsensitiveFieldMixin,
)


class CaseInsensitiveFieldMixin:
    """[summary]
    Mixin to make django fields case insensitive
    """

    def get_prep_value(self, value):
        return str(value).upper()

    def to_python(self, value):
        value = super().to_python(value)

        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.upper()

        return value


class CICharField(CaseInsensitiveFieldMixin, models.CharField):
    pass
