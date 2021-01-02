import os
from sanic import response, Sanic
from utils import cata_rastreio

app = Sanic(__name__)

@app.route("/", methods=["POST", "GET"])
async def index(request):
    lista = []
    for _, _, arquivo in os.walk('image-files'):
        for img in arquivo:
            print('Image Scan now: ' + img)
            lista.append(cata_rastreio.scan_image('image-files/' + img))
            return response.json(lista)

if __name__ == '__main__':
    app.run()