from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, FloatField, RadioField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
    ])
    nombre=StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=10, message="Ingrese nombre valido")
    ])
    apaterno=StringField("APaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno=StringField("AMaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=EmailField("Correo", [
        validators.Email(message="Ingresa correo valido")
    ])

class CinepolisForm(Form):
    nombre=StringField('Nombre:', [
        validators.DataRequired(message="El campo es requerido")
    ])
    compradores=IntegerField('Numero de Compradores:', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingresa al menos un comprador")
    ])
    tarjeta=RadioField(
        '¿Cuenta con tarjeta Cinépolsis?',
        choices=[
           
            ('false', 'No'),
             ('true', 'Sí'),
        ]
    )
    boletos=IntegerField('Numero de Boletos:', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingresa al menos un boleto")
    ])