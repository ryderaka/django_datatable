import datetime
from mongoengine import *
from datatable.models import BaseDocument


class EmbedError(Document, BaseDocument):
    compress_url = StringField(default='', required=True, unique=True)
    url = StringField(required=True)
    error = StringField(default='Something went wrong', required=True)
    status_code = IntField(default=520, required=True)
    timestamp = DateTimeField(default=datetime.datetime.now, required=True)

    meta = {
        'collection': 'embed_errors',
        'indexes': [
            {'fields': ['compress_url'], 'unique': True}
        ]
    }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        if not document.compress_url:
            document.compress_url = encode(document.url)
