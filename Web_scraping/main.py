import requests
import time


r = requests.get("https://github.com/SaumyaKhushlani")



with open("file.html", "w", encoding="utf-8") as f:
    f.write(r.text)
