__author__ = 'John Underwood'

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# driver = webdriver.Chrome('C:/Common/chromedriver',
#                           chrome_options=chrome_options)
#
# driver.get('http://dev.com');
# print(driver.title)
# assert "INDY" in driver.title
#
# time.sleep(3)
# driver.quit()


class Strategy(object):
    def __init__(self, strategy_alternate):
        self.do_exec = strategy_alternate

    def execute(self, arg):
        self.do_exec.execute(arg, self)


class StrategyAbstract(object):
    print("INSIDE StrategyAbstract")


class Login(StrategyAbstract):
    @staticmethod
    def execute(self, arg):
        print(">>> Login ", arg)


class Find(StrategyAbstract):
    @staticmethod
    def execute(self, arg):
        print(">>> Find ", arg)

t = Strategy(Login())
t.execute('arg')
t = Strategy(Find())
t.execute('arg')