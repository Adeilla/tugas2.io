class FileHandler:
 def __init__(self, file_datamahasiswa):
     self.file_datamahasiswa = file_datamahasiswa

 def baca_file(self):
    try: 
        with open(self.file_datamahasiswa, 'r') as file:
            konten = file.read()
            return konten
        
    except FileNotFoundError:
        return f"file {self.file_datamahasiswa} tidak ditemukan" 

 def tulis_file(self, konten, mode):
     with open(self.file_datamahasiswa, mode) as file:
         file.write(konten)
         file.write(mode)
     return f"file {self.file_datamahasiswa} berhasil ditulis"

    