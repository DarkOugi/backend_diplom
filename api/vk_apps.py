import vk_api


def get_access_token(login, password):
    user = vk_api.VkApi(login, password)
    user.auth()
    tokens = user.token['access_token']
    return tokens


def get_user_id(access_token, nickname):
    user = vk_api.VkApi(token=access_token)
    user_api = user.get_api()
    return user_api.users.get(user_ids=nickname)[0]['id']


def get_massage_in_wall(access_token, id_user, count):
    user = vk_api.VkApi(token=access_token)
    user_api = user.get_api()
    items = user_api.wall.get(owner_id=id_user, count=count, filter='owner')['items']
    text = []
    size = 0
    for i in items:
        if count == size:
            break
        else:
            if i['text'] != '' and i['owner_id'] == id_user:
                text.append(i['text'])
                size += 1
    return text


