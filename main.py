from sanic import Sanic
from sanic.response import json, file

from Train.Bot import my_bot

app = Sanic(__name__)
app.static('/static', '/Users/xumingming/Codes/Chat/server/static')

@app.route('/')
async def test(request):
    return await file('/Users/xumingming/Codes/Chat/server/index.html')

@app.route('/get_answer')
def get_answer(request):
    print(request.args)
    q = request.args.get('q', 'hello')
    # q = request.get('q')
    answer = my_bot.get_answer(q)
    print(answer)
    return json({'answer': answer})


app.run(host='0.0.0.0', port=8000, debug=True)