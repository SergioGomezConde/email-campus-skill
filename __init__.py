from mycroft import MycroftSkill, intent_file_handler


class EmailCampus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('campus.email.intent')
    def handle_campus_email(self, message):
        self.speak_dialog('campus.email')


def create_skill():
    return EmailCampus()

