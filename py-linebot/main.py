from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

app = Flask(__name__)

#環境変数取得
accessToken = os.environ[""]
channelSecret = os.environ[""]

# 内部実行用
# accessToken = # access token
# channelSecret = # channel secret

lineBot = LineBotApi(accessToken)
handler = WebhookHandler(channelSecret)

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text = True)
    # app.logger.info("Request body: "  + body)

    #handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    lineBot.reply_message(
        event.reply_token,
        TextSendMessage(
            text = event.message.text
        )
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(
        host = "0.0.0.0", 
        port = port
    )