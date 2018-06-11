from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

class LightSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(LightSkill, self).__init__(name="LightSkill")

    # In this example that means it would match on utterances like:
    #   'Turn on the lights'
    #   'Switch on the light'
    #   'Switch off'
    @intent_handler(IntentBuilder("").require("Switch").require("State").require("What"))
    def handle_light_state(self, message):
        self.speak_dialog("turning.lights", data={"state": message.data["State"]})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

def create_skill():
    return LightSkill()