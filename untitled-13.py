'''import json 
with open('personal.json', 'r', encoding='utf-8') as f: 
    text = json.load(f) 
    text = str(text)'''
result = 'select '
question = input()
main_place = 'from sport s'
data = '*'
if 'вид' in question:
    data = 'section'
elif 'мероприят' in question:
    data = 'section'
elif 'подсекц' in question:
    data = 'subsection'
elif 'соревнован' in question:
    data = 'title'
if 'начал' in question:
    time = 'start'
if 'вс' in question:
    result += place + ' ' + main_place
if 'сколько' in question or 'Сколько' in question or 'количеств' in question:
    result += 'count(' + place + ') '+ main_place
if 'Как' in question:
    result += 'distinct ' + place + ' ' + main_place
print(result)
