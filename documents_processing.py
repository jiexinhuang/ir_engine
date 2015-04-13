from documents import Documents

root = '/Users/jiejingdu/Unimelb/ir_proj1/blogs'

documents = Documents(root)
documents.process()
documents.dump()
