'''import json 
with open('personal.json', 'r', encoding='utf-8') as f: 
    text = json.load(f) 
    text = str(text)'''
result = 'select '
question = input()
main_place = 'from sport s'
data = '*'
if '���' in question:
    data = 'section'
elif '���������' in question:
    data = 'section'
elif '�������' in question:
    data = 'subsection'
elif '����������' in question:
    data = 'title'
if '�����' in question:
    time = 'start'
if '��' in question:
    result += place + ' ' + main_place
if '�������' in question or '�������' in question or '���������' in question:
    result += 'count(' + place + ') '+ main_place
if '���' in question:
    result += 'distinct ' + place + ' ' + main_place
print(result)
