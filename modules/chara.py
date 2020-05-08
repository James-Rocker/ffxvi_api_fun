import requests


def item():
    item_url = 'https://xivapi.com/item/1675?private_key='
    response = requests.get(item_url)
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')
    print(response.json())



# requests.post(url, params=key)


class Character:
    def __init__(self, username, server):
        self.username = username.replace(" ", "+")
        self.server = server
        self.url_short = 'https://xivapi.com/character/'
        self.url = self.url_short + 'search?name=' + self.username + '&server=' + self.server

    def search_data(self):
        response = requests.get(self.url)
        return response.json()

    def avatar(self):
        response = self.search_data()
        value_list = []
        for value in response.values():
            value_list.append(value)
        x = list(map(lambda x: x["Avatar"], value_list[1]))
        return x

    def rank(self):
        response = self.search_data()
        value_list = []
        for value in response.values():
            value_list.append(value)
        x = list(map(lambda x: x["Rank"], value_list[1]))
        return x

    def id(self):
        response = self.search_data()
        value_list = []
        for value in response.values():
            value_list.append(value)
        x = list(map(lambda x: x["ID"], value_list[1]))
        return x


class FullChara(Character):
    def full_chara_data(self):
        chara = self.url_short + " ".join(str(x) for x in self.id()) + '?data'
        response = requests.get(chara)
        return response.json()

    def exp(self):
        response = self.full_chara_data()
        value_list = []
        for value in response.values():
            value_list.append(value)
        for key, value in value_list[1]['ActiveClassJob'].items():
            print(key, value)
        return value_list[1]

    def chara_details(self):
        response = self.full_chara_data()
        value_list = []
        for value in response.values():
            value_list.append(value)
        for key, value in value_list[1].items():
            print(key, value)
        return value_list[1]


print(Character("K'tyr Onye", 'Omega').chara_details())

