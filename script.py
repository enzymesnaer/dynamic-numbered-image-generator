import requests


for i in range(1,131):

    res = requests.get(f'https://dummyimage.com/600x400/fff/000.jpg&text={i}')

    res.raise_for_status()

    yourimagefilevar = open(f'yourimagefile{i}.jpg', 'wb')

    for chunk in res.iter_content(100000):
        yourimagefilevar.write(chunk)
