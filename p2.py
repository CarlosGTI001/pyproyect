import requests
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import pytesseract
import json
import youtube_dl

# Configuración de la ruta del ejecutable de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'  # Reemplaza con la ruta correcta

def get_captcha_text():
    captcha_url = "https://ytlarge.com/youtube/monetization-checker/captcha"
    response = requests.get(captcha_url)
    print(response.content)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(gray)
        # ocr_text = pytesseract.image_to_string(gray)
        # return ocr_text.strip()
    else:
        return None

def make_monetization_request(youtube_url, ocr_text):
    target_url = "https://ytlarge.com/youtube/monetization-checker/channelcheckermain"
    headers = {
        "accept": "*/*",
        "accept-language": "en,es-419;q=0.9,es;q=0.8,es-ES;q=0.7,en-GB;q=0.6,en-US;q=0.5",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {
        "v": youtube_url,
        "deger": ocr_text,
        "mcountry": "en"
    }
    response = requests.post(target_url, headers=headers, data=data, cookies={'cookie_name': 'cookie_value'})
    print(f"Captcha: {ocr_text}")
    return response.text


def get_channel_videos(channel_url):
    ydl_opts = {'quiet': True, 'extract_flat': True, 'force_generic_extractor': True, 'dump_single_json': True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        return info


channel_url = 'https://www.youtube.com/channel/UCUUQerg4QVptE1_2MhELMqg/videos'  # Reemplaza 'CHANNEL_ID' por el ID del canal
channel_info = get_channel_videos(channel_url)

try:
    playlist = json.loads(str(channel_info).replace("'", '"').replace('None', '"None"'))
    file_path = "videos_info.txt"
    with open(file_path, "w") as file:
        for entry in playlist['entries']:
            video_url = f'https://www.youtube.com/watch?v={entry["id"]}'
            file.write(f'URL: {video_url}\n')
            file.write('Respuesta de la solicitud de monetización:\n')
            # Realiza la solicitud de monetización y guarda la respuesta
            ocr_text = get_captcha_text()
            if ocr_text:
                file.write('Texto detectado en el captcha:\n')
                file.write(f'{ocr_text}\n')
                monetization_response = make_monetization_request(video_url, ocr_text)
                file.write(f'{monetization_response}\n')
                file.write('---\n')
    print(f"Se han guardado los detalles de los videos y las respuestas de monetización en {file_path}")
except json.JSONDecodeError as e:
    print("El JSON está mal formateado:", e)
