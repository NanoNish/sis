
from .scripts.keys.keys import handle_key_claim , handle_bro_keys_message
from .scripts.scores.scores import handle_bro_scores_message, handle_user_score
from .scripts.info.info import handle_user_info
from .scripts.google.google_cse import handle_google_image_query,handle_google_animate_query
from .scripts.google import google_maps


def yo(message):
    print("bro.views.yo()")
    return "yo"


def bro(message):
    print("bro.views.bro()")
    return "bro"


def bro_keys_claim(message):
    return handle_key_claim(message)
    

def bro_keys(message): 
    return handle_bro_keys_message(message)

def bro_user_scores(message):
    return handle_user_score(message)

def bro_score_message(message):
    return handle_bro_scores_message(message)

def bro_ping(message):
    return "pong"

def testing_message(message):
    print(message)
    return "test-ed"

def user_info(message):
    return handle_user_info(message)

def google_image_query(message):
    return handle_google_image_query(message)

def google_animate_query(message):
   return handle_google_animate_query(message)

def google_map_query(message):
    return google_maps.handle_google_map_query(message)