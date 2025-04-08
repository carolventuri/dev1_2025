from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from .base_model import BaseModel
from django.db import models
from ..enumerations import Status
from ..validators.cod import CodValidator
from ..validators.funcoes import validate_par
from django.core.exceptions import ValidationError

class Example(BaseModel):
    nome = models.CharField(max_length=100, default=None)
    cod = models.CharField(max_length=10,
                           validators=[MinLengthValidator(10),
                                       CodValidator("444444444"), validate_par],
                           blank=True)
    description = models.CharField(
        max_length=100, null=False, blank=False,
        help_text="Descrição para um exemplo.",
        verbose_name="Descrição",
    )
    quality = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(100)],
        default=50,
        help_text="Valor número para a qualidade do exemplo. Entre 0 e 100.",
        verbose_name="Qualidade",
    )
    balance = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        max_digits=6, decimal_places=2, default=0.00,
        help_text="Saldo financeiro. Valores entre 0 e 1000.",
        verbose_name="Saldo",
    )
    percentage = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.00, null=True, blank=True,
        help_text="Um exemplo de Float. Entre o e 100. Diversas casas decimais.",
        verbose_name="Percentage",
    )
    email = models.EmailField(
        max_length=254, null=False, blank=False, unique=True,
        help_text="E-mail do exemplo.",
        verbose_name="E-mail",
    )
    url = models.URLField(
        max_length=254, null=False, blank=False,
        help_text= "URL externa.",
        verbose_name="URL",
    )
    status = models.CharField(
        max_length=3, null=False, blank=False,
        choices=Status, default=Status.NEW,
        help_text="Selecione o status para o exemplo.",
        verbose_name="Status",
    )

    def __str__(self):
        return f"{self.description} ({self.status}-{self.get_status_display()})" #campo do tipo charfield com choices, libera o metodo get_status_display. mOstra o que está nos parenteses, na classe Status

    class Meta:
        verbose_name = "Exemplo"
        verbose_name_plural = "Exemplos"
        ordering = ("status", "-description",)
        
        
    def clean(self): #para validacoes personalizadas SOMENTE PARA MODELS --- o fullclean serve para VIEWS e TEMPLATES
        if not isinstance(str(self.nome), str):
            raise ValidationError({"nome": "Nome informado é do tipo errado"}, code="error001")
        elif self.nome == "Teste":
            raise ValidationError(
                {"nome": 'Não é possível salvar testes!'},
                code="error002"
            )
        elif self.cod == "1111111111" and self.nome == "IFRS Restinga":
            raise ValidationError(
                {"nome": 'Combinação de nome e código errada!', "cod": 'Combinação de nome e código errada!'},
                code="error0101"
            )
            
        
    def save(self, *args, **kwargs):
        if self.cod is None or self.cod == '':
            letters = string.ascii_letters + string.digits
            self.cod = ''.join(random.choice(letters) for i in range(10))
        super().save(*args,**kwargs)
        
        
        #vou reutilizar? - uso classe
        #se preciso usar dois campos para validar, uso o método clean - validador específico
        #se não vou reutilizar, podemos usar funções