from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	# Incluimos um path vazio e tudo que começar com string vazia nesse path irá utilizar o metodo include e vai para o base folder.
	path('', include('base.urls'))
]
