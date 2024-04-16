from ._anvil_designer import MerakiWifiTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class MerakiWifi(MerakiWifiTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def generate_new_psk_click(self, **event_args):
    """This method is called when the button is clicked"""
    psk, qr = anvil.server.call('generate_new_psk', self.min_len.text, self.max_len.text, self.pass_words.text)
    self.qr_png.source = qr
    self.qr_png.visible = True
    self.network_name.text = "Network Name: TDMDev"
    self.network_password.text = f"Password is {psk}"
    self.network_password.visible = True
    self.network_name.visible = True
    pass

  def get_current_psk_click(self, **event_args):
    """This method is called when the button is clicked"""

    psk, qr = anvil.server.call('get_current_psk')
    # my_media = anvil.BlobMedia(content_type="image/png", content = qr, name= "qr.png" )
    self.qr_png.source = qr
    self.qr_png.visible = True
    self.network_name.text = "Network Name: TDMDev"
    self.network_password.text = f"Password is: {psk}"
    self.network_password.visible = True
    self.network_name.visible = True
    pass
