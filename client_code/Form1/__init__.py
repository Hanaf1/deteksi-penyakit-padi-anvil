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
    result = anvil.server.call("prediksipenyakitpadi",file)
    self.label_2.text = result
    self.image_2.source=file

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    result = anvil.server.call("classify_image",file)
    self.label_hasil.text = result
    self.image_1.source=file
