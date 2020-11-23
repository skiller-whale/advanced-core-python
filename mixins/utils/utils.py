import json
import logging

logging.basicConfig(level=logging.INFO)


def load_document(document):
    location = f"{document['location'][:8]}... {document['location'][-15:]}"
    preview = json.dumps(document['contents'])[:40]
    logging.info(f"Loading document: from {location}: {preview}...")
    ...
    # N.B. This is just a placeholder function for the exercises
