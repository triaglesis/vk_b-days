#! /usr/bin/env python3
# coding=utf-8
__author__ = 'danilcha'
# Change history
# 2015-11-16 Add note about new API method after VK_module update, and new list parsing method.

import vk
from time import gmtime, strftime

curr_date = strftime("%Y-%m-%d")
vk_birth_day = strftime("%d", gmtime())
vk_birth_month = strftime("%m", gmtime())

# TODO:
# New version for Vkontakte api for module ver 2.0a4 and above
token = 'TOKEN'
# session = vk.Session(access_token=token)
vkapi = vk.API(access_token=token)
# vkapi = vk.API(session)

print("Today's date "
      + curr_date +
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
                       group_id=46631810)

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
             " С Ув. администрация Типичного Кировограда. "
             "\n\n"
             "#typical_kirovohrad #birthday@typical_kirovohrad"
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
             "или же не вступили в группу Типичный Кировоград, "
             "поздравление происходит только в том случае, "
             "если все предыдущие условия соблюдены, спасибо за понимание!"
             "#kirovohrad, #kirovograd, #кировоград #кіровоград, "
             "#b_day_bot, #birthday@typical_kirovohrad"
             "\n\n #ВождьБот Powered by #Python made by #trianglesis"
             )

typical_kirovohrad = "-46631810"
typical_kirovohrad_boss = "13147598"

wall_post = vkapi('wall.post',
                  owner_id=typical_kirovohrad,
                  from_group='1',
                  message=greet_msg,
                  attachments='photo-46631810_395130865,'
                              'audio13147598_392954307,'
                              'audio13147598_392954267,'
                              'audio13147598_392954252,'
                              'audio13147598_392954225',
                  signed='0')

print("Message has been posted successfully!")
print(greet_msg)