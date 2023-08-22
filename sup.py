from datetime import date, datetime

print(str(datetime.now()).split(".")[0].replace(" ", "--").replace(":", "-"))