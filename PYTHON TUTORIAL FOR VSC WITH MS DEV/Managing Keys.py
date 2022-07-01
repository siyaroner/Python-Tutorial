import os
os_version=os.getenv("OS")
print (os_version)
# .env is simply going to be a series of key value pairs that
#we're going to use for our environmental variables
# if you add .env in your .gitignore it will provide to aovid accidentally publishing out your .env file
from dotenv import load_dotenv
load_dotenv()
import os
password=os.getenv("PASSWORD") # we won't see this becauese .gitignore won't let to share sensetive data
print (password)
