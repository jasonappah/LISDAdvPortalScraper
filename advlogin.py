import sys, requests

if (len(sys.argv) == 3 or len(sys.argv) == 4 or len(sys.argv) == 5):
    class User:
        def __init__(self, username, password, campus=0):
            self.u = username
            self.ul = len(self.u)
            self.id = self.u[self.ul - 6:self.ul]
            self.p = password
            self.c = campus
            self.url = "https://adv.leanderisd.org/login.aspx?ReturnUrl=%2fDefault.aspx"
            self.h = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': '_ga=GA1.2.195047962.1576415568; nmstat=1576897769856; ASP.NET_SessionId=u4wld3450m1c2y55kkfqonv5;', 'Host': 'adv.leanderisd.org', 'Origin': 'https://adv.leanderisd.org', 'Referer': 'https://adv.leanderisd.org/login.aspx?ReturnUrl=%2fDefault.aspx', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
            


        def data(self):
            return {'__VIEWSTATE': '/wEPDwUJMzgyNjM5OTM4ZGSOU8K+9HMQKr8XIamYxZs2bj5LXg==', '__VIEWSTATEGENERATOR': 'C2EE9ABB','__EVENTTARGET': '', '__EVENTARGUMENT': '', '__EVENTVALIDATION': '/wEWEwK1oo7JAgLwyNvdDgKi9/ChAwLJ4rWJCwKcmrSoAgK5jdaDCAKi5PmeDgLP3pvoAwLosb3DCQKVqN/eDwKcmoSoAgK5jaaDCAKi5MmeDgLP3uvpAwLosY3DCQKVqK/eDwK+g9GpBQKL6ZH3DQL+jNCfD9NY2LurMpl6wg7ea3zWkr2CII4q', 'UsernameTextbox': self.u, 'PasswordTextbox': self.p, 'CampusDropDown': self.c, 'LoginButton': 'Login'}

        def request(self):
            s = requests.Session()
            s.post(self.url, self.data(), self.h)
            return s.get("https://adv.leanderisd.org/Home_Student.aspx")

        def info(self):
            return self.u + "\n" + self.p + "\n" + str(self.c)
    
    if len(sys.argv) == 3:
        student = User(sys.argv[1],sys.argv[2])
    elif (len(sys.argv) == 4 and type(sys.argv[3]) == int):
        student = User(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        student = User(sys.argv[1],sys.argv[2])


    print(student.info())
    r = student.request()
    print(r.text)
    f = open("lADV-"+student.id+".html", "w+")
    f.write(r.text)
    f.close()

    if ("-s" in sys.argv):
        f = open("lADVcreds-"+student.id+".txt", "w+")
        f.write(student.info())
        f.close()

else:
    print("Usage: \n advlogin user pass campusno [-s] - saves credentials to file \n Campus Numbers:" )
    campuses = {'Primary Campus': '0', 'Glenn HS' : '006', 'Wiley MS': ''}
    for campus in campuses:
        print (campus + ": " + campuses[campus])
