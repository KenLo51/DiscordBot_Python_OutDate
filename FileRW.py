import json
from configparser import ConfigParser
def readConfig(fileName):
    cfg = ConfigParser()
    cfg.read('DiscordBotConfig.ini')
    return cfg['DiscordBotConfig']
def readEmoji():
    cfg = ConfigParser()
    cfg.read('emoji.ini')
    emoji=dict([])
    for e in cfg['Emoji']:
        emoji[e] = eval(cfg['Emoji'][e]).decode('utf8')
    return emoji

def readCategory(fileName):
    data = []
    with open(fileName, mode = 'r') as f:
        data = f.read()
    return json.loads(data)

def ReadPollData(fileName):
    with open(fileName,mode='r') as f:
        d = json.load(f.read())
    return d
def SavePollData(fileName,data):
    with open(fileName,mode='w') as f:
        f.write(json.dump(data))
def SaveNewPoll(fileName,data):
    with open(fileName,mode='r+') as f:
        f_data = f.read()
        f_data=json.load(f_data)
        f_data.append(data)
        f.seek(0,0)
        f.write(json.dump(f_data))
def SaveHisPollData(fileName,data):
    with open(fileName,mode='a') as f:
        d = f.write(json.load(data))
    return d

