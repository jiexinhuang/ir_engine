from documents import Documents

root = '/home/jason/ir_engine/blogs'

documents = Documents(root)
documents.process()
documents.dump()
