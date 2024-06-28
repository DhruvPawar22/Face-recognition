import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {

    'databaseURL': "https://face-authentication-real-time-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1":
        {
            "name": "Dhruv Pawar",
            "Major": "Cybersecurity",
            "starting_year": 2021,
            "total_attendance": 1,
            "Standing": "G",
            "year": 3,
            "last_attendance_time": "2024-04-20 00:54:34"
        },
    "2":
        {
            "name": "Sakchu Singh",
            "Major": "CSE CORE",
            "starting_year": 2021,
            "total_attendance": 1,
            "Standing": "G",
            "year": 3,
            "last_attendance_time": "2024-04-20 00:54:34"
        },
    "3":
        {
            "name": "Manish Bangalore",
            "Major": "Cybersecurity",
            "starting_year": 2021,
            "total_attendance": 1,
            "Standing": "G",
            "year": 3,
            "last_attendance_time": "2024-04-20 00:54:34"
        },
    "4":
        {
            "name": "Elon Musk",
            "Major": "Cybersecurity",
            "starting_year": 2021,
            "total_attendance": 1,
            "Standing": "G",
            "year": 3,
            "last_attendance_time": "2024-04-20 00:54:34"
        },


}
for key, value in data.items():
    ref.child(key).set(value)

