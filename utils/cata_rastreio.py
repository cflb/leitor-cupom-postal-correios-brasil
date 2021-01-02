import os
from PIL import Image
import re
import pytesseract

def scan_image(image):
    """
        Vai ler uma imagem e scanear utilizando pytessaract, e vai retorna uma lista com todas as strings capturadas na imagem.
    """
    image = Image.open(image)
    ocr_data = pytesseract.image_to_string(
        image, lang="por").encode('utf-8').split()

    return ocr_data

def get_image_data(ocr_data):
    """
        Recebe uma lista de strings capturadas via scaneamento utilizando scan_image(image).

        Retorna um objeto javascript: 
            {
                'cep': '12345-678',
                'cod-rastreio': 'XX123456789BR' 
            }
    """
    cep_padrao = r"^\d{5}-\d{3}$"
    rastreio_padrao = r"^\w{2}\d{9}\w{2}$"
    cep = re.compile(cep_padrao)
    rastreio = re.compile(rastreio_padrao)

    obje = {}

    for palavra in ocr_data:
        c = cep.findall(palavra.decode("utf-8"))
        r = rastreio.findall(palavra.decode("utf-8"))
        if len(c) > 0:
            obje['cep'] = str(c[0])
        if len(r) > 0:
            obje['cod-rastreio'] = str(c[0])
    return obje


lista = []
for _, _, arquivo in os.walk('image-files'):
    for img in arquivo:
        print('Image Scan now: ' + img)
        result = scan_image('image-files/' + img)
        final_result = (get_image_data(result))
        print(final_result)

        lista.append((get_image_data(result)))
    print(lista)

#jpgs = [arq for arq in arquivos if arq.lower().endswith(".jpg")]