import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'tools')))

from tools.captcha import Captcha

from bs4 import BeautifulSoup
import mechanize, time

class createssh(object):
    def __init__(self, bot, server, group_id, user_id, admin_id):
        self.bot = bot
        self.group_id = group_id
        self.user_id = user_id
        self.admin_id = admin_id
        self.help = """
        Server SSH createssh.
        Server list :
        ======= Server List =========
        Asian
            - Singapura : sg
                - List : 1,2,3
        America
            - United States: usa
                - List : 1,2,3,4,5,6

        ==============================
        Example command request : /ssh createssh sg2, /ssh createssh usa2
        """
        self.url_server = ""
        if server == "usa1":
            self.url_server = "http://createssh.com/premium/registration/create-usa1.php"
        elif server == "usa2":
            self.url_server = "http://createssh.com/premium/registration/create-usa2.php"
        elif server == "usa3":
            self.url_server = "http://createssh.com/premium/registration/create-usa3.php"
        elif server == "usa4":
            self.url_server = "http://createssh.com/premium/registration/create-usa4.php"
        elif server == "usa5":
            self.url_server = "http://createssh.com/premium/registration/create-usa5.php"
        elif server == "usa6":
            self.url_server = "http://createssh.com/premium/registration/create-usa6.php"
        elif server == "sg1":
            self.url_server = "http://createssh.com/premium/registration/create-singapore1.php"
        elif server == "sg2":
            self.url_server = "http://createssh.com/premium/registration/create-singapore2.php"
        elif server == "sg3":
            self.url_server = "http://createssh.com/premium/registration/create-singapore3.php"
        else:
            bot.sendMessage(user_id, "Please check your request.")
            bot.sendMessage(user_id, self.help)

    def generate(self, first_name):
        browser = mechanize.Browser()
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        headers = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1'),
        ]

        browser.addheaders = headers

        browser.open(self.url_server)

        browser.select_form(nr=0)
        browser.form['username'] = first_name+str(int(time.time()))[4:]
        browser.form['password'] = str(int(time.time()))[4:]
        browser.submit()
        soup = BeautifulSoup(browser.response().get_data(), 'lxml')
        return  soup.get_text()