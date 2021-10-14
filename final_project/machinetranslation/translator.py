"""Code for Language Translation"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('sVT65wko-XvBjlwYFj1wr'\
    '_O7OT2I8eiVTq2X8eM50tcQ')
language_translator = LanguageTranslatorV3(version='2021-09-15',authenticator=authenticator)

language_translator.set_service_url('https://api.au-syd.language'\
    '-translator.watson.cloud.ibm.com/instances/1d050083-269a-4f2f-ba04-077cd5880889')

languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))


def english_to_french(english_text):
    """Language translation from English to French"""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    #french_text = print(json.dumps(translation, indent=2, ensure_ascii=False))
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Language translation from English to French"""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    #english_text = json.dumps(translation, indent=2, ensure_ascii=False)
    english_text = translation['translations'][0]['translation']
    return english_text

english_to_french("Hello!")
french_to_english("Bonjour!")
