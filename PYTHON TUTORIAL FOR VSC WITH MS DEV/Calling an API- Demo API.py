""" When a developer wnats to share the functionality of a function but
not the actual code in the program, they can place the function
on a web server. A programmer with the address of that function on the web
web server and the reguired permissions can cal the function.
What is an API    
You can't call a function unless you know the function name and the required parameters
when you create a web service you create an Aplication Programmming Interface (API).
The API defines the funciton names and parameters so others know how to call your funtion.
e.g.   analyze (visualfeatures, details, language) 
Keys allow me to track which users have permission to use my service and
A developer signs up on my web site or buys a license for my software and is provided a unique key
When the developer calls my web service they provide their unique key and unique and I'm
able to verify the key has been approved fo calls to my web service and

There is a standart for sneding messages across the web
Hypertext Transfer Protocol (HTTP) is a standard protocol for sendening messages across the web.
- Get 
  . Pass values in query string only
  . Special characters must be "escaped"
  . Limited amount of data

-Post
  . Pass values in query string and body
  . No need to escape special characters if passed in body
  . Can pass large amounts of data, including images in body
https://westus.dev.cognitive.microsoft.com/docs/services

The request library simplifies HTTP calls from python code
requests.post(adress, http_headers, function_parameters, message_body)"""

# Demo
"""This code will show you how to call Computer Vision API from python. You can find documentation on the Computer Vision  Analyze Image method
here: 
https://westus.dev.cognitive.microsoft.com/docs/services/56f91f2d778daf23d8ec6739/operations/56f91f2e778daf14a499e1fa

"""
#Use the request library to simplify making a REST API call from python

import requests

# WE will need the json library to read the data passed back by the web service

import json
#We need the key to acces our computer vision service
SUBSCRIPTION_KEY= "bee12db25dfd42e884c5d23442b01aaf"

# We need the address of our computer vision service (the syntax is:
# https://{endpoint}/vision/v2.0/analyze)
vision_service_address= "https://mlandcv.cognitiveservices.azure.com/vision/v2.0/analyze"

# Add the name of the function we want to call to the address
address= vision_service_address+"vision/v2.0/analyze"
""" According to the documention for the analyze image function there are three optional parameters: language, details and visualFeatures
"""
parameters= {"visualFeatures":"Description,Color","language":"en"}

#open the image file to get a file object containing the image to Analyze
image_path="./image/kitten.jpg"
image_data= open(image_path,"rb").read()


"""According to the documentation for the analyze image function  we need to specify the subscription key and the content type
in the HTTP header, Content Type is application/octet-stream when you pass in a j"""
headers= {"Content-Type":"application/octet-stream", 
          "Ocp-Apim-Subscription-key":SUBSCRIPTION_KEY}

"""According to the documentation for the analyze image function we use HTTP POST to call this function"""
response= requests.post(address, headers=headers, params= parameters, data=image_data)

#Raise an exception if the call returns an error code
#response.raise_for_status()

#Display the Json results returned
results=response.json()
print(json.dumps(results))



