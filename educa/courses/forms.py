from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module

# набор форм
# inlineformset_factory позволяет создавать
# модельный набор форм динамически для объектов Module, связанных
# с объектом Course.
ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=['title',
                                              'description'],
                                      extra=2,  # число пустых дополнительных форм
                                      can_delete=True)
