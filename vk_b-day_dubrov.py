#! /usr/bin/env python3
# coding=utf-8
__author__ = 'danilcha'
# Change history
# 2015-11-16 Add note about new API method after VK_module update, and new list parsing method.

import vk
import datetime

today = datetime.date.today()
tomorrow = (today + datetime.timedelta(days=1))
vk_birth_day = today.strftime("%d")
vk_birth_month = today.strftime("%m")

# TODO:
# New version for Vkontakte api for module ver 2.0a4 and above
token = 'TOKEN'
# session = vk.Session(access_token=token)
vkapi = vk.API(access_token=token)
# vkapi = vk.API(session)

print("Today's date "
      + str(today) +
      " will find b-days for this day."
      "Day string is "
      + vk_birth_day +
      ". Month string is "
      + vk_birth_month +
      " continue"
      )

users_birthday = vkapi('users.search',
                       count=1000,
                       birth_day=vk_birth_day,
                       birth_month=vk_birth_month,
                       group_id=72808168)

users_id = users_birthday['items']

# TODO:
# New version of users list extracting from api result
# This is not two dicts, it's now one list with index[0] = count of items
# users_birthday.pop(0)

all_bdays = len(users_id)
some = []
for user in users_id:
    for vk_id in user:
        id_int = user['id']
        id_str = str(id_int)
        for raw_id in id_str:
            all_str = str("@id" + id_str)
            for line in all_str:
                some.append(all_str)
                break
            break
        break

count = len(some)
those_ids = ', '.join(some)

print("How many b-day-ers were found:")
print(count)
print("\n")
print("Composing greeting message")

greet_msg = ("Поздравляем наших подписчиков с днём рождения!"
             "\n\n"
             "Желаем Вам всего самого лучшего!"
             "\n\n"
             " С Ув. администрация Подслушано в Бобровице. "
             "\n\n"
             + those_ids +
             "\n\n"
             " от: Бот автоматического поздравления"
             "\n\n"
             "\n\n"
             "\n\n"
             "Если вы не попали в список, значит, "
             "вероятно вы или закрыли свою дату рождения, "
             "или заполнили её некорректно, "
             "или же не вступили в группу Подслушано в Бобровице, "
             "поздравление происходит только в том случае, "
             "если все предыдущие условия соблюдены, спасибо за понимание!"
             "#b_day_bot"
             "\n\n #ВождьБот Powered by #Python made by #trianglesis"
             )

dubrovitsa = "-72808168"
Kran = "72036088"
martynenko = "18758942"
domlatov = "293694073"

wall_post = vkapi('wall.post',
                  owner_id=dubrovitsa,
                  from_group='1',
                  message=greet_msg,
                  attachments='photo-72808168_406834136',
                  signed='0')

print("Message has been posted successfully!")
print(greet_msg)