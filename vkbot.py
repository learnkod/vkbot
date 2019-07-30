import vk_api 
vk=vk_api.VkApi(token="8271bf73e5a1f577ef5d71d1790da7f3ab375b1d3d515a1e3ad9dfdd26247690190bbb0d63d82d18abf83")

import vk_api
import time
import random
 
token = "8271bf73e5a1f577ef5d71d1790da7f3ab375b1d3d515a1e3ad9dfdd26247690190bbb0d63d82d18abf83"
 
vk = vk_api.VkApi(token=token)
 
vk._auth_token()
 
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "хатю спать":
                vk.method("messages.send", {"peer_id": id, "message": "Спокойной ночи!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "оюна":
                vk.method("messages.send", {"peer_id": id, "message": "Оюна хорошая, Оюна не злая сука^^!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "рома":
                vk.method("messages.send", {"peer_id": id, "message": "ето бох ^-^!", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "нипанятна", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)