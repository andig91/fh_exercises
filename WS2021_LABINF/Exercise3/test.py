import time

print(time.strftime("%Y/%m/%d %H:%M:%S"))

serviceKosten = {'Erwachsene': 25, 'Studierende': 18, 'Kinder': 12, "Sauna": 5, "Private SPA": 10, 'kein Service': 0}
abzug = 0

abzug += serviceKosten['Erwachsene']

import datetime
today = datetime.date.today()
someday = datetime.date(2008, 12, 25)
diff = someday - today
print(diff.days)



while True:
    print("1")
    while True:
        print("2")
        time.sleep(1)
        break
        print("3")
    