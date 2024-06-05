from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Properti untuk menyimpan file yang diunggah
    self.uploaded_file = None

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    # Simpan file yang diunggah ke properti
    self.uploaded_file = file
    # Tampilkan nama file di label_2
    self.label_2.text = f"File uploaded: {file.name}"

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.uploaded_file:
      # Jika file telah diunggah, tampilkan nama file di label_2
      self.label_2.text = f"File loaded: {self.uploaded_file.name}"
    else:
      # Jika tidak ada file yang diunggah, tampilkan pesan di label_2
      self.label_2.text = "No file uploaded"
