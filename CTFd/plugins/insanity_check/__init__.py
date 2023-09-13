from flask import Blueprint

from CTFd.models import (
    ChallengeFiles,
    Challenges,
    Fails,
    Flags,
    Hints,
    Solves,
    Tags,
    db,
)
from CTFd.plugins import register_plugin_assets_directory
from CTFd.plugins.challenges import CHALLENGE_CLASSES, BaseChallenge

class InsaneChallenge(BaseChallenge):
    id = "insane"  # Unique identifier used to register challenges
    name = "insane"  # Name of a challenge type
    
    # locations of the html templates
    templates = {  # Handlebars templates used for each aspect of challenge editing & viewing
        'create': '/plugins/insanity_check/assets/create.html',
        'update': '/plugins/insanity_check/assets/update.html',
        'view': '/plugins/insanity_check/assets/view.html',
    }

    # location of the JavaScript files
    scripts = {  # Scripts that are loaded when a template is loaded
        'create': '/plugins/insanity_check/assets/create.js',
        'update': '/plugins/insanity_check/assets/update.js',
        'view': '/plugins/insanity_check/assets/view.js',
    }

    challenge_model = Challenges



def load(app):
    CHALLENGE_CLASSES["insane"] = InsaneChallenge
    register_plugin_assets_directory(app, base_path='/plugins/insanity_check/assets/')