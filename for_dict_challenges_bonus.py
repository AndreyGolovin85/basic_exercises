"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [None, (random.choice([m["id"] for m in messages]) if messages else None), ],
            ),
            "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def user_id_by_max_messages(messages: list) -> str:
    """
    Вывести айди пользователя, который написал больше всех сообщений.
    :param messages: list
    :return: str
    """
    count_id_users = {}
    for message in messages:
        id_user = message["sent_by"]
        if id_user in count_id_users:
            count_id_users[id_user] += 1
        else:
            count_id_users[id_user] = 1

    return f"Написал больше всех сообщений: {max(count_id_users, key=lambda user: count_id_users[user])}."


def user_id_message_where_answer(messages: list) -> str:
    """
    Вывести айди пользователя, на сообщения которого больше всего отвечали.
    :param messages: list
    :return: str
    """
    count_id_users = {}
    for message in messages:
        id_user = message["sent_by"]
        reply_for = message["reply_for"]
        if id_user in count_id_users:
            if reply_for is None:
                count_id_users[id_user] += 0
            else:
                count_id_users[id_user] += 1
        else:
            count_id_users[id_user] = 1
    return f"Пользователь, на сообщения которого больше всего отвечали: " \
           f"{max(count_id_users, key=lambda user: count_id_users[user])}."


def user_id_message_seen_by(messages: list) -> str:
    """
    Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
    :param messages: list
    :return: str
    """
    users_seen_messages = {}
    for message in messages:
        if message['sent_by'] not in users_seen_messages:
            users_seen_messages[message['sent_by']] = []

    for message in messages:
        users_seen_messages[message['sent_by']] += message['seen_by']

    count_users_seen_messages = {}
    for user_id, seen_by in users_seen_messages.items():
        count_users_seen_messages[user_id] = len(set(seen_by))

    return ", ".join([str(key) for key in count_users_seen_messages
                      if count_users_seen_messages[key] == max(count_users_seen_messages.values())])


def user_id_sent_at(messages: list) -> str:
    """
    Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18
    часов). morning, afternoon, evening.
    :param messages: list
    :return: str
    """
    messages_chat_sent_at = {}
    for message in messages:
        date_time = message["sent_at"]
        hour = date_time.hour
        # Здесь пока ничего лучше не придумал.
        ######################################################
        morning = "morning"
        afternoon = "afternoon"
        evening = "evening"
        if 6 <= hour < 12:
            if morning in messages_chat_sent_at:
                messages_chat_sent_at[morning] += 1
            else:
                messages_chat_sent_at[morning] = 1

        if 12 <= hour < 18:
            if afternoon in messages_chat_sent_at:
                messages_chat_sent_at[afternoon] += 1
            else:
                messages_chat_sent_at[afternoon] = 1

        if hour >= 18:
            if evening in messages_chat_sent_at:
                messages_chat_sent_at[evening] += 1
            else:
                messages_chat_sent_at[evening] = 1
        #####################################################

    return f"В чате больше всего сообщений: " \
           f"{max(messages_chat_sent_at, key=lambda time: messages_chat_sent_at[time])}."


if __name__ == "__main__":
    # print(generate_chat_history())
    print(user_id_by_max_messages(generate_chat_history()))
    print(user_id_message_where_answer(generate_chat_history()))
    print(
        f"Айди пользователей, сообщения которых видело больше всего уникальных пользователей: "
        f"{user_id_message_seen_by(generate_chat_history())}")
    print(user_id_sent_at(generate_chat_history()))
