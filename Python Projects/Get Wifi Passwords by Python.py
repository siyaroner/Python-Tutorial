# import subprocess

# data=subprocess.check_output(["netsh","wlan","show","profiles"])
# data= data.decode("ISO-8859-1").split("\n")
# profiles=[profile.split(":")[1][1:-1] for profile in data if "All User Profile" in profile]
# print("{:<40}| {:}\n".format("Wi-Fi Names","Passwords"))
# for profile in profiles:
#     data=subprocess.check_output(["netsh","wlan","show","profiles"])
#     data=data.decode("ISO-8859-1").split("\n")
    
#     passwords=[passw.split(":")[1][1:-1] for passw in data if "Key Content" in passw]
    
#     try:
#         print("{:<20}| {:}".format(profile,passwords[0]))
#     except IndexError:
#         print("{:<20}| {:}".format(profile,""))   
        
        
        
        
        
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('ISO-8859-1').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('ISO-8859-1').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
input("")