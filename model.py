import pyrebase
#from firebase_details import link_to_firebase

###### Firebase Connections ############

def connect_to_firebase():
    config = {
        "apiKey": "AIzaSyCbfuvreUeRFO11cwrcOCKrd6v_xE5dGEw",
        "authDomain": "multi-dimensional-cj.firebaseapp.com",
        "databaseURL": "https://multi-dimensional-cj-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "multi-dimensional-cj",
        "storageBucket": "multi-dimensional-cj.appspot.com",
        "messagingSenderId": "406315615131",
        "appId": "1:406315615131:web:84ba8240b63a015e7c973e",
        "measurementId": "G-9FWWWLTX60"
    }

    firebase = pyrebase.initialize_app(config)

    return firebase


def init_db():
    firebase    = connect_to_firebase()
    firebase_db = firebase.database()

    return firebase_db


def init_auth():
    firebase      = connect_to_firebase()
    firebase_auth = firebase.auth()

    return firebase_auth


def init_storage():
    firebase         = connect_to_firebase()
    firebase_storage = firebase.storage()

    return firebase_storage