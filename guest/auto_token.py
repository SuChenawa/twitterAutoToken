from selenium import webdriver
import json
driver=webdriver.PhantomJS()
driver.get('https://mobile.twitter.com/kanomahoro')
data=json.dumps(driver.get_cookie('gt'))
with open('token.json','w',encoding='utf-8') as fp:
    fp.write(data)
driver.close()
driver.quit()