from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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
    predictdisease = anvil.server.call('predict_disease',self.uploaded_file)
    """This method is called when the button is clicked"""
    if predictdisease:
      # Jika file telah diunggah, tampilkan nama file di label_2
      self.label_2.text = f"penyakit tanaman padi : {predictdisease.capitalize()}"
    else:
      # Jika tidak ada file yang diunggah, tampilkan pesan di label_2
      self.label_2.text = "No file uploaded"

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    hasil = anvil.server.call("say_hello", self.text_box_1.text)
    self.label_hasil.text = hasil

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call("classify_image",file)
    self.label_hasil.text = result
    self.image_1.source=file
