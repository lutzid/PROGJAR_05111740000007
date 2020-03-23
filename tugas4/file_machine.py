from file import File
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- put : untuk upload file
  request : put
  parameter : filename
  response : berhasil -> ok
             gagal -> error

- download : untuk download file
  request: download
  parameter : filename
  response: berhasil -> OK
            gagal -> ERROR

- list : untuk melihat daftar file yang telah diupload
  request: list
  parameter: tidak ada
  response: list file yang telah diupload

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
f = File()

class FileMachine:
    def proses(self, string_to_process):
        s = string_to_process
        print(string_to_process)
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            print(command)
            if (command == 'put'):
                logging.warning("put")
                filename = cstring[1].strip()
                file_content = cstring[2].strip()
                f.put(filename, file_content.encode())
                return "OK"
            elif (command == 'download'):
                logging.warning("download")
                filename = cstring[1].strip()
                hasil = f.download(filename)
                return hasil[0]
            elif (command == 'list'):
                logging.warning("list")
                filename = f.list_files()
                hasil = {"files" : filename}
                return json.dumps(hasil, indent=4)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = FileMachine()
    hasil = pm.proses("list")
    print(hasil)
    hasil = pm.proses("download test.py")
    print(hasil)