import json
import os

from mycroft import MycroftSkill, intent_file_handler

# Fichero JSON donde almacenar la informacion
ficheroJSON = "/home/serggom/scraping/datos.json"


class EmailCampus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('campus.email.intent')
    def handle_campus_email(self, message):

        # Lectura de la informacion del fichero JSON
        if os.path.exists(ficheroJSON):

            # Lectura de la informacion del fichero JSON
            with open(ficheroJSON) as ficheroUsuario:
                data = json.load(ficheroUsuario)
                for user in data['usuario']:
                    self.speak(
                        "Su dirección de correo electrónico de la Universidad de Valladolid es: " + user['email'])

            ficheroUsuario.close()

        else:
            self.speak("Lo siento, no dispongo de esa información")


def create_skill():
    return EmailCampus()
