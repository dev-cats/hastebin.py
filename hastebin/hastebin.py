from requests import post


def post(content, url='https://hastebin.com'):
    post = post(f'{url}/documents', data=content.encode('utf-8'))
    return url + '/' + post.json()['key']
