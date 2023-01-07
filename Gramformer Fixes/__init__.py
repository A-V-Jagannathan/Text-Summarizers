from importlib import import_module
import spacy
from errant.annotator import Annotator

# ERRANT version
__version__ = '2.3.3'

# Load an ERRANT Annotator object for a given language
def load(lang, nlp=None):
    # Make sure the language is supported
    supported = {"en_core_web_sm"}
    if lang not in supported:
        raise Exception("%s is an unsupported or unknown language" % lang)

    # Load spacy
    nlp = nlp or spacy.load(lang)

    # Load language edit merger
    merger = import_module("errant.en_core_web_sm")

    # Load language edit classifier
    classifier = import_module("errant.en_core_web_sm")
    # The English classifier needs spacy
    if lang == "en_core_web_sm": classifier.nlp = nlp

    # Return a configured ERRANT annotator
    return Annotator(lang, nlp, merger, classifier)
