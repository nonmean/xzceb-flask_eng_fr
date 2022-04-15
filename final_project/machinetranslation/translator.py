"""
language translator using IBM watson API
"""

# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#print(apikey)
#print(url)

# init translator
# task 1.9
def init_language_translator():
    """
    :return: instance of the language translator
    """
    authenticator = IAMAuthenticator(apikey)
    translator = LanguageTranslatorV3(
        version="2018-05-01",
        authenticator=authenticator)

    translator.set_service_url(url)

    translator.set_disable_ssl_verification(True)

    return translator


language_translator = init_language_translator()


# task 1.10
def english_to_french(english_text):
    """
    :param english_text: input english text
    :return: output french text
    """
    #write the code here
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()


    french_text = translation["translations"][0]["translation"]

    return french_text


# taks 1.11
def french_to_english(french_text):
    """
    :param frenchText: input french text
    :return: output english text
    """
    #write the code here
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    english_text = translation["translations"][0]["translation"]

    return english_text
