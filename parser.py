import vk
import json
import time

session = vk.Session(access_token='6a99b6dce7c59daac6a76e3703ab3b75b6ddc9f4ee569c9ef1173c07cee4638d2c47e9eab2c22753863af')
api = vk.API(session, v='5.101', lang='ru', timeout=10)

zapros = 'Город' #тип запроса
attribute_str = '1' # запрос в формате идентификатора (город, университет, школа), числа (возраст от), либо строки (место работы)
attribute_str_2 =  '1' # доп. атрибут (для типа запроса 'возраст')
n = 1000
s = 0
frnds2 = list([s])
attribute = {
    'Город': api.users.search(city = attribute_str, count = n),
    'Возраст': api.users.search(age_from = int(attribute_str), age_to = int(attribute_str_2), count = n),
    'Школа': api.users.search(school = int(attribute_str), count = n),
    'Университет': api.users.search(university = int(attribute_str), count = n),
    'Место работы': api.users.search(company = attribute_str, count = n),
}
users = attribute[zapros]
users = users.pop('items')
for i in  range(n):
    time.sleep(0.33)
    usr = users.pop()
    usr = usr.pop('id')
    frnds = api.friends.get(user_id = usr)
    frnds = frnds.pop('items')
    frnds2.extend(frnds)
    frnds2.append(usr)
frnds2.remove(0)
frnds2 = list(set(frnds2))

while (frnds2):
    time.sleep(1)
    usr = str(frnds2.pop())
    user = api.users.get(fields='city, photo_100 ,sex, country, last_seen, schools, universities', user_ids=usr) # информация о пользователе (json)
    #print(user)
    closed = user
    closed = closed.pop()
    closed = closed.get('is_closed',True)
    if  not closed:
        frnds = api.friends.get(user_id = usr) # список друзей пользователя (list)
        #print(frnds)
