import asyncio
import time
import os
from walkoff_app_sdk.app_base import AppBase

class Logmall(AppBase):
    __version__ = "1.0.0"
    app_name = "logmall"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):

        super().__init__(redis, logger, console_logger)

    async def sell(self, name, sub_name,log):
        try:
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
        except:
            mystr = "no selenium"
            return mystr
        option = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=/Users/apple/Library/Application Support/Google/Chrome/Default')
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-gpu')
        option.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(chrome_options=option)
        # browser=webdriver.Chrome()

        if log == 'yes' or log == 'y':
            os.system('sshpass -p hitimc@ics scp 10.245.142.242:/home/log/shuffle_log.txt /')
            time.sleep(5)
            os.system('echo mall is running... ------start time: `(date +%Y-%m-%d_%H:%M:%S)` >> shuffle_log.txt')
        browser.get("http://10.245.142.98")
        browser.set_window_size(1920, 1080)
        browser.maximize_window()
        browser.find_element_by_name("password").send_keys("macro123")
        browser.find_element_by_name("password").send_keys(Keys.ENTER)
        time.sleep(2)

        browser.find_element_by_xpath("/html/body/div/div/div[1]/div/ul/div/li[1]/div").click()#sell
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div/div/div[1]/div/ul/div/li[1]/ul/a[2]/li').click()
        time.sleep(2)

        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div/div/div[2]/form/div[1]/div/span/span').click()#type
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[2]/ul/li[1]').click()
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[2]/ul[2]/li[1]').click()
        time.sleep(1)

        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div/div/div[2]/form/div[2]/div/div[1]/input').send_keys(name)
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div/div/div[2]/form/div[3]/div/div/input').send_keys(sub_name)
        time.sleep(1)

        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div/div/div[2]/form/div[4]/div/div/div/input').click()#brand
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        time.sleep(1)


        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div/div/div[2]/form/div[13]/div/button/span').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div/div/div[3]/form/div[17]/div/button[2]').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div/div/div[4]/form/div[6]/div/button[2]/span').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div/div/div[5]/form/div[3]/div/button[2]/span').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[2]/span').click()
        time.sleep(2)
        ret=10086
        if log == 'yes' or log == 'y':
            os.system('echo mall has finished... ------finish time: `(date +%Y-%m-%d_%H:%M:%S)` >> shuffle_log.txt')
            ret=os.system('sshpass -p hitimc@ics scp /shuffle_log.txt 10.245.142.242:/home/log/')
        return "OK!!"+str(ret)


if __name__ == "__main__":
    asyncio.run(Logmall.run(), debug=True)
