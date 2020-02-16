from mycroft import MycroftSkill, intent_file_handler


class Diploma(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('diploma.intent')
    def handle_diploma(self, message):
        self.speak_dialog('diploma')


def create_skill():
    return Diploma()

