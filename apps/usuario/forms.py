from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

class RegistroForm(UserCreationForm):
	captcha = ReCaptchaField(widget=ReCaptchaWidget(attrs={'class':'validate'}),label="")

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
			]
		labels = {
				'username': 'Nombre de Usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
		}