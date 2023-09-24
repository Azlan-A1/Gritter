import pymongo
from pymongo import MongoClient
import hashlib

cluster = MongoClient("mongodb+srv://rchwiec:hckYRocks3@cluster0.zes7f.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Main"]
collection = db["Main"]

def hash_Input(input_string):
    byte_string = input_string.encode()
    sha256 = hashlib.sha256()
    sha256.update(byte_string)
    return sha256.hexdigest()

def is_Email_Taken(Email):
    if (collection.find_one({"Email":Email}) is None):
        return False
    return True

def insert_New_User(Email, password, first_name, last_name):
    #were first going to encrypte the password recieved
    if (is_Email_Taken(Email)):
        return False
    password_encrypted =  hash_Input(password)
    user_info = {"Email":Email,"Password":password_encrypted,"First_name":first_name,"Last_name": last_name}
    collection.insert_one(user_info)
    return True

def update_User(Email, Attribute, updated):
    if not(is_Email_Taken(Email)):
        return False
    collection.update_one({"Email":Email},{"$set":{Attribute:updated}})
    return True

def get_User(Email):
    if not(is_Email_Taken(Email)):
        return False
    return collection.find_one({"Email":Email})

def delete_User(Email):
    if not(is_Email_Taken(Email)):
        return False
    collection.delete_one({"Email":Email})
    return True
