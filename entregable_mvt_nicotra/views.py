from django.http import HttpResponse
from django.template import loader
from app_familia.models import Familia


def familia(self):
    familiar = Familia(nombre = "Nestor", relacion = "padre", edad = "62", fecha_nacimiento = "1959-11-21")
    familiar.save()

    familiar_1 = Familia(nombre = "Marisa", relacion = "madre", edad = "63", fecha_nacimiento = "1959-06-02")
    familiar_1.save()

    familiar_2 = Familia(nombre = "Belen", relacion = "concubina", edad = "24", fecha_nacimiento = "1998-02-28")
    familiar_2.save()

    plantilla = loader.get_template("familia.html")

    familiares = [familiar, familiar_1, familiar_2]
    
    documento = plantilla.render({"familiares":familiares})

    return HttpResponse(documento)





