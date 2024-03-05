import json,datetime,pytz

def load_json(name):
  try:
    with open(f'data/{name}.json', mode='r', encoding="utf8") as jFile:
      jdata = json.load(jFile)
    print(jdata)
    jFile.close()
    return jdata
  except:
    with open(f'data/{name}.json', mode='w', encoding="utf8") as jFile:
      jFile.write("{}")
      jFile.close()
    with open(f'data/{name}.json', mode='r', encoding="utf8") as jFile:
      jdata = json.load(jFile)
    return jdata

def write_js(name,data):
  jsdata = json.dumps(data,ensure_ascii=False)
  with open(f'data/{name}.json', mode='w', encoding="utf8") as jFile:
    jFile.write(jsdata)
    jFile.close()

def now_time():
    current_time = datetime.datetime.now()
    timezone = pytz.timezone('Asia/Taipei')
    localized_time = current_time.astimezone(timezone)
    return localized_time.strftime("%Y-%m-%d %H:%M")