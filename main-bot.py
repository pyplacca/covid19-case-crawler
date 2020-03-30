import crawler, json

Request = crawler.Request
urlopen = crawler.urlopen

TG_URL = 'https://api.telegram.org/bot{}'
paths = {
    'send': {
        'message': '/sendMessage?chat_id={chat_id}&text={message}'
    },
    'get': '/getUpdates'
}


with open('token.txt', 'r') as tkn:
    TG_URL = TG_URL.format(tkn.readline())


def get_json_data(obj):
    try:
        return json.load(obj)
    except AttributeError:
        return json.loads(obj)

def get_updates():
    update = crawler.get_url_response(f"{TG_URL}{paths['get']}")
    return get_json_data(update)

def send_message(id_, msg):
    output = paths['send']['message'].format(
        chat_id=id_, message=msg
    )
    return crawler.get_url_response(f"{TG_URL}{output}")

print(get_json_data(
    crawler.get_url_response(
        f"{TG_URL}{paths['get']}"
    )
))
