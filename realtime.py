import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd

class RealTimeDataCall:
    def __init__(self):
       pass
    
    def runtimeCall(self):
        # Fetching the service account key JSON file
        cred = credentials.Certificate("serviceKey.json")
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred, {
                "databaseURL": "https://hash-4e554-default-rtdb.firebaseio.com"
            })

        # Read careers data
        ref_read_careers = db.reference("form/careers/")
        json_req_careers = ref_read_careers.get()

        marks_arr, branch_arr, location_arr = [], [], []
        for key, val in json_req_careers.items():
            marks_arr.append(val["Marks"])
            branch_arr.append(val["branch:"])
            location_arr.append(val["location"])

        realtime = []
        for i in range(len(marks_arr)):
            realtime.append([marks_arr[i], branch_arr[i], location_arr[i]])

        df = pd.DataFrame(realtime, columns=['Marks', 'Branch', 'location'])
        df.to_csv("careers_real_time.csv", encoding='utf-8-sig', index=False)

        # Read courses data
        ref_read_courses = db.reference("form/courses/")
        json_req_courses = ref_read_courses.get()

        interest_arr, location_arr, duration_arr = [], [], []
        for key, val in json_req_courses.items():
            interest_arr.append(val["Interested"])
            location_arr.append(val["Location"])
            duration_arr.append(val["Duration"])

        realtime = []
        for i in range(len(interest_arr)):
            realtime.append([interest_arr[i], location_arr[i], duration_arr[i]])

        df = pd.DataFrame(realtime, columns=['Interested', 'Location', 'Branch'])
        df.to_csv("courses_real_time.csv", encoding='utf-8-sig', index=False)

        # Read job data
        ref_read_job = db.reference("form/job/")
        json_req_job = ref_read_job.get()

        age_arr, location_arr, curr_arr, str_arr, exp_arr, sal_arr, hob_arr = [], [], [], [], [], [], []
        for key, val in json_req_job.items():
            age_arr.append(val["Age"])
            location_arr.append(val["Location"])
            curr_arr.append(val["Current Qualification"])
            str_arr.append(val["Strength"])
            exp_arr.append(val["Experience"])
            sal_arr.append(val["Salary Expectation"])
            hob_arr.append(val["Hobbies"])

        realtime = []
        for i in range(len(age_arr)):
            realtime.append([age_arr[i], location_arr[i], curr_arr[i], str_arr[i], exp_arr[i], sal_arr[i], hob_arr[i]])

        df = pd.DataFrame(realtime, columns=['Age', 'Location', 'Current Qualification', "Strength", "Experience", "Salary Expectation", "Hobbies"])
        df.to_csv("job_real_time.csv", encoding='utf-8-sig', index=False)