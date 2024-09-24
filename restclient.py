# This is sample code for rest client (GET, CREATE, UPDATE, DELETE)
# API Server link:  https://restful-booker.herokuapp.com/apidoc/index.html

import requests
from requests import auth
import json

from requests.auth import HTTPBasicAuth


class RestClient:
    def __init__(self, baseURL, uname, passwd):
        self.baseURL = baseURL
        if uname:
            self.uname = uname
        else:
            self.uname = "admin"
        if passwd:
            self.passwd = passwd
        else:
            self.passwd = "password123"

    def getmethod(self, endpoint):
        url = self.baseURL + str(endpoint)
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(e)

    def postmethod(self, endpoint, body):
        url = self.baseURL + endpoint
        msgbody = body
        header = {"Accept":"application/json", "Content-Type":"application/json", "Accept-Encoding":"gzip, deflate, br"}
        try:
            response = requests.post(url=url, data=msgbody, headers=header)
            if response.status_code == 200:
                return response.json()
            else:
                return [ response.status_code, response.content ]
        except Exception as e:
            print(e)

    def putmethod(self, endpoint, body):
        url = self.baseURL + str(endpoint)
        msgbody = body
        header = {"Accept":"application/json", "Content-Type":"application/json", "Accept-Encoding":"gzip, deflate, br"}
        try:
            response = requests.put(url=url, data=msgbody, headers=header, auth=HTTPBasicAuth(self.uname, self.passwd))
            if response.status_code == 200:
                return "Update PASS"
            else:
                return response.status_code
        except Exception as e:
            print(e)

    def deletemethod(self, endpoint):
        url = self.baseURL + str(endpoint)
        try:
            response = requests.delete(url=url, auth=HTTPBasicAuth(self.uname, self.passwd))
            if response.status_code == 201:
                return response.raw
        except Exception as e:
            print(e)


obj_restclient = RestClient("https://restful-booker.herokuapp.com/booking/", "", "")

#Get all the objects
print("******************** Get all objects *******************************")
response_get = obj_restclient.getmethod("")
print(response_get)


#Create new object
print("\n****************** Create new Object ***************************** ")
try:
    messagebody = '{ "firstname": "Shikhar", "lastname": "J", "totalprice": 111, "depositpaid": "true", "bookingdates": { "checkin": "2018-01-01", "checkout": "2019-01-01" }}'
    response_create = obj_restclient.postmethod(endpoint="", body=messagebody )
    print(response_create)
    bookingid = response_create['bookingid']
except Exception as e:
    print("Object not created" + str(e))



#update an object
print("\n****************** Update an Object ***************************** ")
try:
    updatemessagebody = '{ "firstname": "Shikhar", "lastname": "J", "totalprice": 300, "depositpaid": "true", "bookingdates": { "checkin": "2018-01-01", "checkout": "2020-01-01" }}'
    print("Before Update: ")
    beforeupdate = obj_restclient.getmethod(endpoint=bookingid)
    print(beforeupdate)
    response_update = obj_restclient.putmethod(endpoint= bookingid,
                                               body=updatemessagebody)
    afterupdate = obj_restclient.getmethod(endpoint=bookingid)
    print("After Update: " + response_update)
    print(afterupdate)
except Exception as e:
    print("object not updated")



#delete object
print("\n****************** Delete an object ***************************** ")
try:
    obj_restclient.deletemethod(endpoint=bookingid)
    print("Object Deleted: " + str(bookingid) )
except Exception as e:
    print("Object not deleted: \n" + str(e))