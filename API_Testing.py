# -> * API-Communications * <-

# <*> Key Elements <*>
import requests

# -> Checking with API
def ping_Cloud_API():
    try:
        api_Response = requests.get("https://randomuser.me/api?$select=gender,name,first")
        statusCode = str(api_Response.status_code)
        print(" \nStatus: " + statusCode)
    except:
        print(" \nStatus: " + statusCode)
    return api_Response

# -> Pulling Json objects from response
def reply_Json(api_Response):
    api_ReplyJson = api_Response.json()
    return api_ReplyJson

# -> Declaring values
api_Reply = ping_Cloud_API()
api_Json = reply_Json(api_Reply)

# -> Checking reponse data
gender = api_Json["results"][0]["gender"]
first_Name = api_Json["results"][0]["name"]["first"]
last_Name = api_Json["results"][0]["name"]["last"]

print(" \n" + gender + " \n" + first_Name + " " + last_Name + "\n ")