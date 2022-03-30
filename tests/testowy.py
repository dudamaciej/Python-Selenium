import os
ebook = "test"
print(os.path.join (os.path.dirname(os.path.dirname (__file__)), "download", ebook + ".pdf"))