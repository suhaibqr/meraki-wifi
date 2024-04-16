from ._anvil_designer import MerakiWifiTemplate
from anvil import *
import anvil.server

class MerakiWifi(MerakiWifiTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def generate_new_psk_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('generate_new_psk', self.min_len, self.max_len, self.pass_words)
    pass

  def get_current_psk_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('get_current_psk')
    pass
