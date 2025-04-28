# morphopretext/__init__.py
import inspect
from inspect import getfullargspec as _getfullargspec, formatargvalues

def getargspec(func):
    spec = _getfullargspec(func)
    return spec.args, spec.varargs, spec.varkw, spec.defaults

# no-op: new NLTK won’t need formatargspec
inspect.getargspec    = getargspec
inspect.formatargspec = lambda *a, **k: ""

# back-populate Iterable for parsivar’s old imports
import collections
from collections.abc import Iterable
collections.Iterable = Iterable

# ─── morphopretext exports ────────────────────────────────────────────────────
from .Dictionaries_En            import english_dict
from .Dictionaries_Fa            import arabic_dict
from .english_text_preprocessor  import EnglishTextPreprocessor
from .persian_text_preprocessor  import PersianTextPreprocessor

__all__ = [
    "english_dict",
    "arabic_dict",
    "EnglishTextPreprocessor",
    "PersianTextPreprocessor",
]
