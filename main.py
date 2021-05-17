
import requests

url = "http://omenarea.com/auth.php" 
#the phishing url that posts the requests


data = {
  "doAuth" : "1",
  "login" : "sdsdasdasdasdasdasd",
  "password" : "sdsdsasdasdasdasd",
}
#data that will be passed as login info 

i=0
while(True):
  response1 = requests.post(url , data = data) #post method to spam data on thier database
  i+=1
  print(response1.status_code, i) #just print how many times the code ran (200 means success and then the number means no of iteration)