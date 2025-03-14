import requests
import os


if not os.path.exists("jpgs"):
    os.makedirs("jpsgs")
    
dir = os.listdir("jpgs")

for i in dir:
    try:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(fr"jpgs/{i}", 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': ''},
        )
        if response.status_code == requests.codes.ok:
            if not os.path.exists("pngs"):
                os.makedirs("pngs")
            with open(fr"pngs/{i}", 'wb') as out:
                out.write(response.content)
        else:
            print("Erro:", response.status_code, response.text)

    except Exception as e:
        print(e)

