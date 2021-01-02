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
        print(r)
        print(c)
        if len(c) > 0:
            obje['cep'] = c[0]
        if len(r) > 0:
            obje['cod-rastreio'] = r[0]
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

#data = [b'ida', b'apos', b'6', b'hor\xc3\xa1rio', b'Vinite', b'de', b'"VCR', b'(UNA,', b'Sera', b'acrescidostotum', b'dia', b'util', b'ao', b'pr', b'820', b'padr\xc3\xa3o', b'de', b'entrega', b'INPRESSO', b'REG', b'NODICO', b'|', b'Valor', b'do', b'Porte(hk$),,:', b'16,90', b'Cep', b'Destino:', b'39740-000', b'(NMG/GuAnhaes)', b'20,10+', b'Peso', b'real', b'(G).......', b';', b'1745', b'Peso', b'Tarifados.....o.',b':', b'1,7145', b'OBJETO====22225>', b'RE737536730BR', b'REGISTRO', b'MODICO', b'\xc3\x80', b'VT;', b'3,20', b'Postagem', b'ocorrida', b'apos', b'o', b'horario', b'linite', b'de', b'paost', b'agen', b'(DH),', b'sera', b'acrescido', b'|', b'(um)', b'dia', b'util', b'ao', b'pr', b'azo', b'padrao', b'de', b'entrega', b"'e..........", b'A', b'VPILINNKER', b'PAA', b'A', b'2E', b'a', b'ocA', b'RA', b'TATAI', b'hn']

#final_result = (get_image_data(data))
#print(final_result)