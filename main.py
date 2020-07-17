import json
from PIL import Image 
import requests
import time
from colorama import Fore, Back, Style 
foundcard = ""
#https://github.com/public-apis/public-apis/blob/master/README.md

site = 'https://db.ygoprodeck.com/api/v5/cardinfo.php'
#this will be modified with the text
r = requests.get(site)
text = r.text
card = json.loads(text)
# a list of all the names of the cards

cardnames = []
cards1 = []
allmonsters = []
allspells = []
alltraps = []

for i in range(len(card)):
  cardnames += ([card[i]["name"]])
  if (card[i]["type"] == 'Spell Card'):
    minidict = [{"id": card[i]["id"],
   "name": card[i]["name"], "type": card[i]["type"], "desc": card[i]["desc"], "race": card[i]["race"],}]
    allspells += minidict
  
  elif (card[i]["type"] == 'Trap Card'):
    minidict = [{"id": card[i]["id"],
   "name": card[i]["name"], "type": card[i]["type"], "desc": card[i]["desc"], "race": card[i]["race"],}]
    alltraps += minidict

  elif (card[i]["type"] == 'Normal Monster') or (card[i]["type"] == 'Effect Monster') or (card[i]["type"] == 'Ritual Monster') or (card[i]["type"] == 'Fusion Monster') or (card[i]["type"] == 'Xyz Monster') or (card[i]["type"] == 'Synchro Monster') or (card[i]["type"] == 'Link Monster') or (card[i]["type"] == 'Pendulum Monster') or (card[i]["type"] == 'Monster Token'):
    if (card[i]["type"] == 'Link Monster'):
      minidict = [{"id": card[i]["id"], "name": card[i]["name"], "type": card[i]["type"], "desc": card[i]["desc"],  "linkval": card[i]["linkval"], "linkmarkers": card[i]["linkmarkers"], "race": card[i]["race"], "attribute": card[i]["attribute"], "atk": card[i]["atk"]}]
    elif (card[i]["type"] == 'Pendulum Monster'):
      [{"id": card[i]["id"], "name": card[i]["name"], "type": card[i]["type"], "desc": card[i]["desc"],  "linkvalm": card[i]["linkval "], "linkmarkers ": card[i]["linkmarkers "], "race": card[i]["race"], "attribute": card[i]["attribute"], "scale": card[i]["scale"], "atk": card[i]["atk"], "def": card[i]["def"]}]
    else:
      minidict = [{"id": card[i]["id"], "name": card[i]["name"], "type": card[i]["type"], "desc": card[i]["desc"],  "def": card[i]["def"], "atk": card[i]["atk"], "level": card[i]["level"], "race": card[i]["race"], "attribute": card[i]["attribute"]}]
    allmonsters += minidict
  cards1.append(minidict)

  if minidict[0]["type"] == "Spell Card":
    print(Fore.GREEN + Back.RESET + str([card[i]["name"]]))
  elif minidict[0]["type"] == "Trap Card":
    print(Fore.MAGENTA + Back.RESET + str([card[i]["name"]]))
  elif minidict[0]["type"] == "Synchro Monster":
    print(Fore.WHITE + Back.RESET + str([card[i]["name"]]))
  elif minidict[0]["type"] == "Link Monster":
    print(Fore.CYAN + Back.RESET + str([card[i]["name"]]))
  elif minidict[0]["type"] == "Fusion Monster":
    print(Fore.MAGENTA + Back.RESET + str([card[i]["name"]]))
  elif minidict[0]["type"] == 'Xyz Monster':
    print(Fore.BLACK + Back.WHITE + str([card[i]["name"]]))
  elif minidict[0]["type"] == 'Ritual Monster':
    print(Fore.BLUE + Back.RESET + str([card[i]["name"]]))
  elif minidict[0]["type"] == 'Pendulum Effect Monster' or minidict[0]["type"] == 'Pendulum Normal Monster':
    print(Fore.CYAN + Back.RESET + str([card[i]["name"]]))
  elif minidict[0]["type"] == 'Effect Monster':
    print(Fore.RED + Back.RESET + str([card[i]["name"]]))
  elif minidict[0]["type"] == 'Normal Monster':
    print(Fore.YELLOW + Back.RESET + str([card[i]["name"]]))
  else:
    print(Fore.RED + Back.RESET + str([card[i]["name"]]))
  time.sleep(0.002)

def sortmonster(spellcardlist):
  pass
