from PIL import Image
from urllib.request import urlopen
from colorama import Fore, Back, Style 

class CardClient():
  #__init__() is called when you create an Object class
  def __init__(self, id, name, card_type, desc, race, archetype, image_url, small_image_url):
    #stores argument in self
    self.id = id
    self.name = name
    self.card_type = card_type
    self.desc = desc
    self.race = race
    self.archetype = archetype
    self.image = image_url
    self.small_image = small_image_url
      
  def display_image(self):
    img = Image.open(urlopen(self.image))
    img.show()
  
  def display_small_image(self):
    img = Image.open(urlopen(self.small_image))
    img.show()

  def display_card_card_type_with_color(self):
    if self.card_type == "Spell Card":
      print(Fore.GREEN + Back.RESET + self.name + Fore.RESET)
    elif self.card_type == "Trap Card":
      print(Fore.MAGENTA + Back.RESET + self.name + Fore.RESET)
    elif self.card_type == "Synchro Monster":
      print(Fore.WHITE + Back.RESET + self.name + Fore.RESET)
    elif self.card_type == "Link Monster":
      print(Fore.BLUE + Back.RESET + self.name + Fore.RESET)
    elif self.card_type == "Fusion Monster":
      print(Fore.MAGENTA + Back.RESET + self.name + Fore.RESET)
    elif self.card_type == "Xyz Monster":
      print(Fore.BLACK + Back.RESET + self.name + Fore.RESET)
    elif self.card_type == "Ritual Monster":
      print(Fore.BLUE + Back.RESET + self.name + Fore.RESET)
    elif self.card_type == "Pendulum Effect Monster" or self.card_type == "Pendulum Normal Monster":
      print(Fore.CYAN + Back.RESET + self.name + Fore.RESET)
    elif self.card_type == "Effect Monster":
      print(Fore.RED + Back.RESET + self.name + Fore.RESET)
    elif self.card_type == "Normal Monster":
      print(Fore.YELLOW + Back.RESET + self.name + Fore.RESET)
    else:
      print(Fore.RED + Back.RESET + self.name + Fore.RESET)