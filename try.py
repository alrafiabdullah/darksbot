import json
from datetime import datetime, timezone

# All the code tryouts

'''with open('infos/riot_id.json', "r") as riot:
    data = json.load(riot)

with open('infos/riot_id.txt', 'w') as text:
    for i in range(len(data['riot_id'])):
        text.write(data['riot_id'][i]["Name"] + " : " + data['riot_id'][i]["Riot_ID"] + "\n")
text.close()

with open('infos/riot_id.txt', 'r') as text:
    print(text.read())
text.close()

def date_formatter(timestamp):
    datetime = ""
    formatted_month = ""
    year = timestamp[0:4]
    month = timestamp[5:7]
    day = timestamp[8:]

    if (month == "01"):
        formatted_month = "January"
    elif (month == "02"):
        formatted_month = "February"
    elif (month == "03"):
        formatted_month = "March"
    elif (month == "04"):
        formatted_month = "April"
    elif (month == "05"):
        formatted_month = "May"
    elif (month == "06"):
        formatted_month = "June"
    elif (month == "07"):
        formatted_month = "July"
    elif (month == "08"):
        formatted_month = "August"
    elif (month == "09"):
        formatted_month = "September"
    elif (month == "10"):
        formatted_month = "October"
    elif (month == "11"):
        formatted_month = "November"
    elif (month == "12"):
        formatted_month = "December"

    datetime = day + " " + formatted_month + ", " + year

    return datetime


arrived = "2020-06-07"
formated_arrived = date_formatter(arrived)
print (formated_arrived)

count = 0
line_count = 0
num = 0

with open('infos/riot_id.txt', "r", encoding="UTF-8") as memberlist_file:

    for line in memberlist_file:
        line_count += 1
        for ch in line:
            count += 1
memberlist_file.close()
print("Character in file: " + str(count) + " Line in file: " + str(line_count))

demo = "abc#1234"
position_value = demo.find('4')
print(len(demo))
print(position_value)

if (position_value<len(demo) and position_value >= 0):
    checker = True
else:
    checker = False

print(checker)


demo = ["@everyone", "Dark's Validator Bot", "Battle Bot", "Testers", "Mod", "Dev"]

for d in demo:
    print(d[-3:].lower())


game_list = ["PUBG", "Grand Theft Auto V", "VALORANT", "Overwatch", "VALORANT", "PUBG"]

new_list = list(dict.fromkeys(game_list))

print(game_list)
print(new_list)

from datetime import datetime

timestamp_ms = 1374148087974

output_time = datetime.fromtimestamp(round(timestamp_ms/1000))

print(output_time)

print(output_time.strftime("%d-%m-%Y %I:%M %p"))'''

server_created_at = datetime(2019,10,7, tzinfo=timezone.utc)

year = int(datetime.utcnow().year - server_created_at.year)
month = (datetime.utcnow().month - server_created_at.month) - 1


if month<0:
    month*=-1
    print("Month is negative")
date = (datetime.utcnow().day - server_created_at.day)
if date<0:
        date += 30

print(datetime.now().month)
print("Year: " + str(year) + " Month: " +  str(month) + " Days: " + str(date))