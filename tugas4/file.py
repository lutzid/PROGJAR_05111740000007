import os
import base64
import shelve
import uuid


class File:
    def __init__(self):
        if not os.path.exists("file_database"):
            os.makedirs("file_database")
    def put(self, filename = None, file_content = None):
        # path = os.path.dirname(os.path.abspath(__file__))
        data = file_content
        f = open("file_database/" + filename, "wb")
        f.write(base64.b64decode(data))
        return True
    def download(self, filename = None):
        temp = []
        # path = os.path.dirname(os.path.abspath(__file__))
        f = open('file_database/' + filename, "rb")
        file_content = f.read()
        f.close()
        hasil = base64.b64encode(file_content)
        temp.append(hasil.decode())
        return temp
    def list_files(self):
        lf = []
        for filename in os.listdir("file_database"):
            lf.append("{ filename: " + filename + "}")
        return lf

if __name__=='__main__':
    p = File()
    #print(p.download("test.py"))
    #print(p.list_files())
