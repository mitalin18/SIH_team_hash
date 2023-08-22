import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

class Uploader:
    def __init__(self):
        # Fetching the service account key JSON file
        cred = credentials.Certificate("serviceKey.json")
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred, {
                "databaseURL": "https://hash-4e554-default-rtdb.firebaseio.com"
            })

        # Saving the data
        ref = db.reference("contact/")
        self.users_ref = ref.child("data")
    
    def upload(self, name, email, ph, mssg):
        now = str(datetime.now()).split(".")[0].replace(" ", "--").replace(":", "-")

        self.users_ref.update({
            now: {
                "Name": name,
                "email:": email,
                "phone": str(ph),
                "message": str(mssg)
            }
        })
    
    # def upload_career(self, arr):
    #     now = str(datetime.now()).split(".")[0].replace(" ", "--").replace(":", "-")

    #     ref = db.reference("form/")
    #     users_ref = ref.child("careers")

    #     users_ref.update({
    #         now: {
    #             "coding": arr[0],
    #             "biology:": arr[1],
    #             "physics": arr[2],
    #             "chemistry": arr[3],
    #             "maths": arr[4],
    #             "science": arr[5],
    #             "commerce": arr[6],
    #             "ssc": arr[7],
    #             "hsc": arr[8],
    #         }
    #     })
    
    def upload_career(self, arr):
        now = str(datetime.now()).split(".")[0].replace(" ", "--").replace(":", "-")

        ref = db.reference("form/")
        users_ref = ref.child("careers")

        users_ref.update({
            now: {
                "location": arr[0],
                "branch:": arr[1],
                "Marks": arr[2],
               # "chemistry": arr[3],
                #"maths": arr[4],
                #"science": arr[5],
                #"commerce": arr[6],
                #"ssc": arr[7],
                #"hsc": arr[8],
            }
        })
    
    def upload_job(self, arr):
        now = str(datetime.now()).split(".")[0].replace(" ", "--").replace(":", "-")

        ref = db.reference("form/")
        users_ref = ref.child("job")

        users_ref.update({
            now: {
                "Age": arr[0],
                "Location": arr[1],
                "Current Qualification": arr[2],
                "Strength": arr[3],
                "Experience": arr[4],
                "Salary Expectation": arr[5],
                "Hobbies": arr[6],
               # "Mental Health": arr[7],
                #"Analytical Skills": arr[8],
            }
        })
    
    def upload_courses(self, arr):
        now = str(datetime.now()).split(".")[0].replace(" ", "--").replace(":", "-")

        ref = db.reference("form/")
        users_ref = ref.child("courses")

        users_ref.update({
            now: {
                "Interested": arr[0],
                "Location": arr[1],
                "Duration": arr[2],
               # "domain of interest": arr[3],
                #"duration of course": arr[4],
            }
        })

# upl = Uploader()
# arr = [f"{i}" for i in range(9)]
# upl.upload_job(arr)

