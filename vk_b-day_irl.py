#!/usr/bin/env python3
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
token = '_TOKEN_'
# session = vk.Session(access_token=token)
vkapi = vk.API(access_token=token)
# vkapi = vk.API(session)

print("Today's date "
      +curr_date+
      " will find b-days for this day."
      "Day string is "
      +vk_birth_day+
      ". Month string is "
      +vk_birth_month+
      " continue"
      )

users_birthday = vkapi('users.search',
                       count=1000,
                       birth_day=vk_birth_day,
                       birth_month=vk_birth_month,
                       from_list='friends')
users_id = users_birthday['items']

# TODO:
# New version of users list extracting from api result
# This is not two dicts, it's now one list with index[0] = count of items
# users_birthday.pop(0)

some = []
if users_id:
    print(users_id)
    for user in users_id:
        for vk_id in user:
            id_int = user['id']
            id_str = str(id_int)
            for raw_id in id_str:
                all_str = str("@id"+id_str)
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

    greet_msg = ("Поздравляю с днем рождения! "+those_ids)
    # photo266810306_379885011, audio266810306_391727152, audio266810306_391727151, audio266810306_391727150
    wall_post = vkapi('wall.post',
                      owner_id='266810306',
                      from_group='1',
                      message=greet_msg,
                      attachments='photo266810306_379885011, '
                                  'audio266810306_391727152, '
                                  'audio266810306_391727151, '
                                  'audio266810306_391727150',
                      signed='0')

    print("Message has been posted successfully!")

else:
    print("Nobody born today")