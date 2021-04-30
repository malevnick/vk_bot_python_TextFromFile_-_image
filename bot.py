import traceback
from vk_api import VkApi, VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

if __name__ == '__main__':
    vk = VkApi(token='токен от группы')
    upload = VkUpload(vk)
    longpoll = VkBotLongPoll(vk, 'id группы')
    api = vk.get_api()

    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    peer_id = event.obj.message['peer_id']
                    text = event.obj.message['text']

                    print(peer_id, text)

                    with open('text.txt', 'r') as f:
                        msg = f.read().strip()

                    img = upload.photo_messages('test.jpg', peer_id)[0]
                    img = f'photo{img["owner_id"]}_{img["id"]}'

                    if text.lower() == 'logs':
                        m = api.messages.send(
                            peer_id = peer_id,
                            random_id = 0,
                            message = msg,
                            attachment = img
                        )

        except Exception as e:
            traceback.print_exc()
