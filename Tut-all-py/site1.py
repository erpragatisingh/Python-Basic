import requests
with requests.Session() as c:
    url = "WEBSITE URL (LOGIN PAGE)"
    USERNAME = "valid username"
    PASSWORD = "valid password"
    c.get(url)
    login_data = dict(username=ISERNAME, password=PASSWORD, next='/')
    c.post(url, data=login_data, headers={"Referer":"HOMEPAGE"})
    page = c.get("PROTECTED LEVEL OF WEBSITE")
    print (page.content)
