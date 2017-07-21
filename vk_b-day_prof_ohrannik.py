#! /usr/bin/env python3
# coding=utf-8
__author__ = 'Dasha'
# Change history
# 2015-11-16 Add note about new API method after VK_module update, and new list parsing method.

import vk
from time import gmtime, strftime

all_time = strftime("%Y-%m-%d")
vk_birth_day = strftime("%d",gmtime())
vk_birth_month = strftime("%m",gmtime())

vkapi = vk.API(access_token='TOKEN')
# vkapi = vk.API(session)

# New version for Vkontakte api for module ver 2.0a4 and above
# session = vk.Session(access_token='a2f872776a18112f7630cc33efc2e10797b500437b08da0609c8ae7623c6f6fc8ce5027093216f7e3ac1d')
# vkapi = vk.API(session)

users_birthday = vkapi('users.search',
                  count = 1000,
                  birth_day = vk_birth_day,
                  birth_month = vk_birth_month,
                  group_id = 75174667)

users_id = users_birthday['items']

some_inf = []
if users_id:
    # print(users_id)
    for user in users_id:
        for vk_id in user:
            id_int = user['id']
            id_str = str(id_int)
            for raw_id in id_str:
                all_string = str("@id" + id_str)
                for each in all_string:
                    some_inf.append(all_string)
                    break
                break
            break

    those_ids = ', '.join(some_inf)
    profohrannik_id = "-75174667" #put id of group prof_ohrannik
    profohrannik_boss_id = "4744443" #id of my account vk Dashka Pislar
    message_text = (

                    "Сегодня мы поздравляем с Днем рождения участников группы [club75174667|Профессия-охранник!]"
                    "\n\n"
                    +those_ids +
                    "\n\n"
                    " Желаем вам крепкого здоровья, удачи и спокойных смен!"
                    "\n\n"
                    "Если у тебя сегодня тоже День рождения, укажи дату рождения в своем профиле,"
                    " чтобы мы знали, когда тебя поздравлять!"
                    "\n\n"
                    "#профессияохранник #prof_ohrannik"
                    "\n\n"
                     )

    wall_post = vkapi ('wall.post',
    owner_id = profohrannik_id,
    from_group = '1',
    message = message_text,
    attachments = 'photo-75174667_392500988,'
                  'audio-75174667_418530374,',
    signed = '0')

    one_last_post_list = []
    get_list = []

    get_last_one_post = vkapi('wall.get',
    owner_id= profohrannik_id,
    domain= 'prof_ohrannik',
    count=1,
    filter='all',
    extended='0')
# print(get_last_one_post)
    one_last_post_list.append(get_last_one_post['items'])
    # print(one_last_post_list)

    for dicts in one_last_post_list:
        for dict in dicts:
            get_list.append(dict)
# print(get_list)
        last_one_id = []
        if get_list:
            for post in get_list:
                wall_post_id_int = post['id']
                wall_post_id = str(wall_post_id_int)
                # print(get_list)
                for one_id in wall_post_id:
                    last_one_id.append(wall_post_id)
                    # print(last_one_id)
                    break


        wall_post_fix = vkapi ('wall.pin',
        owner_id = profohrannik_id,
        post_id = last_one_id)
        # print(wall_post_fix)

# 3652






















    # wall_post_fix = vkapi ('wall.pin',
    # owner_id = profohrannik_id,
    # from_group = '1',
    # message = message_text,
    # attachments = 'photo-75174667_392500988,'
    #               'audio-75174667_418530374,',
    # signed = '0',
    # post_id = '1')
    # print(wall_post_fix)




    # wall_post = vkapi ('wall.pin',
    # owner_id = profohrannik_id,
    # from_group = '1',
    # message = message_text,
    # attachments = 'photo-75174667_392500988,'
    #               'audio-75174667_418530374,',
    # signed = '0',
    # post_id = '1')