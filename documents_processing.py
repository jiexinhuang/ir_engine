from documents import Documents

root = '/home/jason/ir_engine/small'

documents = Documents(root)
documents.process()
documents.dump()
