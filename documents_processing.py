from documents import Documents
from config import settings

documents = Documents(settings['blogs_root'])
documents.process()
documents.dump()
