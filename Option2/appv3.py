from flask import Flask, request, abort
from discord_webhook import DiscordWebhook


app = Flask(__name__)

l1 = "new"
l2 = "new"
l3 = "new"
l4 = "new"
l5 = "new"

olds = {"1": l1, "2": l2, "3":l3, "4":l4, "5":l5}

@app.route('/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        
        if request.json != None:
            
            message = request.json['text']
            global olds
            _text = str(message).split(' ')

            for i in olds.keys():
                if _text[1][:1] == i:

                    if message!= olds[i]:
                        olds[i]=message
                        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1038881162417950830/oOTmdax58j8kss0y57nL7-Hcdov3QEgzGbE9u4VM47NrBXZQCB_LbVwImJXiYrGrPtse', content=message)
                        response =webhook.execute()    

                    else:
                        print('Message not unique.\n\n\n')

            return "Webhook received!"

        else:
            _string = "Input was of type None\n\n\n"
            print(_string)
            return _string

        
    else:
        abort(400)



if __name__ == "__main__":
    app.run(host='0.0.0.0')

# app.run(host='0.0.0.0', port=80)



#{"text": "LIST 1: bearish signals: [BINANCE:HNTUSDTPERP], no bullish signals in this list."}
#{"text": "LIST 2: bearish signals: [BINANCE:SOLUSDTPERP], no bullish signals in this list."}
#{"text": "LIST 3: bearish signals: [BINANCE:DRDUSDTPERP], no bullish signals in this list."}
#{"text": "LIST 4: bearish signals: [BINANCE:BTCUSDTPERP], no bullish signals in this list."}
#{"text": "LIST 5: bearish signals: [BINANCE:FTTUSDTPERP], no bullish signals in this list."}

