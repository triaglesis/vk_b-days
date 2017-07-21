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

group_tk = '46631810'
group_inga = '66592289'

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
                       group_id=group_tk)

# users_id = users_birthday
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

if count:
    print("How many b-day-ers were found:")
    print(count)
    print("\n")
    print("Composing greeting message")

    greet_msg = ("Поздравляем наших подписчиков с днём рождения!"
                 "\n\n"
                 "Дарим вам скидку 15% на любую процедуру!"
                 "\n\n"
                 "Детальнее читайте на странице."
                 "\n\n"
                 + those_ids +
                 "\n\n"
                 "\n\n"
                 "\n\n"
                 "\n\n"
                 "#kirovohrad, #kirovograd, #кировоград, #кіровоград, #b_day_bot,"
                 "\n\n #ВождьБот Powered by #Python made by #trianglesis"
                 )

    link = 'https://vk.com/page-66592289_51113278,'
    photo = 'photo-66592289_380959424,'
    music = 'audio13147598_392954307,audio13147598_392954267,audio13147598_392954252,audio13147598_392954225'
    inga_beauty = '-66592289'
    page = 'page-66592289_51113278'

    wall_post = vkapi('wall.post',
                      owner_id=inga_beauty,
                      from_group='1',
                      message=greet_msg,
                      attachments=photo+page+music,
                      signed='0')

    print("Message has been posted successfully!")
else:
    print("No B-daers found today!")