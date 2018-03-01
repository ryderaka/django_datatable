from pymongo.errors import BulkWriteError, DuplicateKeyError


class BaseDocument:
    @classmethod
    def insert_many(cls, documents, ordered=True, bypass_document_validation=False, skip_duplicate_key_error=False,
                    **kwargs):
        documents = [doc.to_mongo() for doc in documents]
        try:
            cls._get_collection().insert_many(documents, ordered, bypass_document_validation, **kwargs)
        except (BulkWriteError, DuplicateKeyError) as e:
            if not skip_duplicate_key_error:
                raise e

    @staticmethod
    def update_embedded_documents(documents, update, where):
        if isinstance(update, dict) and isinstance(where, dict):
            for doc in documents:
                found = True

                for key in where:
                    if hasattr(doc, key) and getattr(doc, key) != where[key]:
                        found = False
                        break

                if found:
                    for key in update:
                        setattr(doc, key, update[key])

        return documents


from .models import *
