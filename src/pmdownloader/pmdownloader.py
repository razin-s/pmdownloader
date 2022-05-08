import os
import requests


def download(url, path='', file_name=''):
    if file_name == '':
        file_name = url.split('/')[-1]
    r = requests.get(url, stream=True)
    name = path + file_name
    try:
        os.makedirs(path)
    except:
        pass
    with open(name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
    return f"Downloaded: {file_name}"
