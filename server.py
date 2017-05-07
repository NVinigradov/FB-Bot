# During writing this bot was used materials
# from articles how to create your own bot in the FB
# in the Enternet with codes
import requests
from flask import Flask, request, app
import json
import bot
import logging
from flask import Flask, request

app = Flask(__name__)
desk = list(range(0, 9))
class Bot:


    def execute(self, message, sender):
        logging.info("\nSender: {}\nMessage: {}".format(sender, message))
        command = message.split()[0].lower()
        if (str(command) in "012345678"):
            win = False
            cnt = 0
            while not win:
                command = message.split()[0].lower()
                bot.FieldToDraw(desk)
                if cnt % 2 == 0:
                    bot.talkingWithPlayer(command)
                else:
                    yield("Bot`s turn")
                    bot.SetZero()
                cnt += 1
                if cnt > 4:
                    tmp = bot.If_Win(desk)
                    if tmp:
                        yield(tmp, "won")
                        win = True
                        break
                if cnt == 9:
                    yield("nodoby won")
                    break
                bot.FieldToDraw(desk)

logging.basicConfig(filename='info.log',
                    filemode='w',
                    level=logging.DEBUG)
def handle_verification():
    return request.args['hub.challenge']


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', methods=['GET'])
def get_user_info(T, id):
    request = requests.get("https://graph.facebook.com/v2.6/" + id,
                           params={"fields": "first_name,last_name", "access_token": T})
    if not (request.status_code == requests.codes.ok):
        logging.error(request.text)
    return json.loads(request.content)


def sending(rec, t):
    request = requests.post("https://graph.facebook.com/v2.6/me/messages", params={"access_token"},
                            data=json.dumps({
                                "recipient": {"id": rec},
                                "message": {"text": t}
                            }), headers={'Content-type': 'application/json'})
    if not (request.status_code == requests.codes.ok):
        logging.error(request.text)


def messaging_events(payload):
    data = json.loads(payload)

    if 'entry' not in data or 'messaging' not in data['entry'][0]:
        return

    msg = data["entry"][0]["messaging"]

    for event in msg:
        if "message" in event and "text" in event["message"]:
            yield event["sender"]["id"], event["message"]["text"]
        elif 'sender' in event:
            yield event['sender']['id'], None


if __name__ == '__main__':
    logging.info("App started.")
    app.run()
