import requests
import json

from api.config import auth, api

token = ''


# авторизация
def authorization():
    global token
    auth_param = json.dumps(auth)
    print(auth_param)
    path = api['address'] + api['port'] + '/user/auth'
    print(path)
    r = requests.post(path, data=auth_param)
    try:
        token = r.headers['authorization']
    except Exception:
        print('Incorrect config')
    print('current_token : ' + token)


# создание документа
def create_document(title):
    data = {
        "name": title,
        "public": True,
        "template": False
    }

    if token == '':
        print('Not authorization user')
        return

    header = {
        'Authorization': token
    }
    path = api['address'] + api['port'] + '/document'
    r = requests.post(path, headers=header, data=json.dumps(data))
    print(r.content)


# список документов
def doc_list():
    if token == '':
        print('Not authorization user')
        return
    header = {
        'Authorization': token
    }
    path = api['address'] + api['port'] + '/user/docs'
    r = requests.get(path, headers=header)
    # print(r.json())
    result = r.json()
    return result


# вывод документа
def get_doc(doc_id):
    if token == '':
        print('Not authorization user')
        return
    header = {
        'Authorization': token
    }
    path = api['address'] + api['port'] + '/document/' + str(doc_id)
    r = requests.get(path, headers=header)
    print(r.json())
    result = r.json()
    return result


# добавить новый блок
def insert_block(doc_id, title, content, ord):
    if token == '':
        print('Not authorization user')
        return
    header = {
        'Authorization': token
    }
    data = {
        'doc_id': doc_id,
        'name': title,
        'content': content,
        'order': ord
    }

    path = api['address'] + api['port'] + '/document/edit'
    r = requests.post(path, headers=header, data=json.dumps(data))
    print(r.json())
    return r.json()


authorization()
