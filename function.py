import firebase_admin
from firebase_admin import credentials, db
import time

cred = credentials.Certificate('firebase-adminsdk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://python-flask-b40d3.firebaseio.com/'
})


def _serial():
    timestampt = int(time.time()*1000.0)
    return str(timestampt)


def post():
    id = _serial()
    data = {
        'nama': 'Siti',
        'kelas': 'VIII'
    }
    ref = db.reference('siswa').child(id).update(data)
    print('Success')
    return ref


def get():
    id = _serial()
    ref = db.reference('siswa').order_by_child('id').get()
    print(ref)


if __name__ == '__main__':
    # post()
    get()
