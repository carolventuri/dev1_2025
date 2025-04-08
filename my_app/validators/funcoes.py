from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _ 

def validate_par (valor):
    if int(valor) % 2 !=0:
        raise ValidationError (
            _("O número informado deve ser par."),
            params={"valor":valor}
        )