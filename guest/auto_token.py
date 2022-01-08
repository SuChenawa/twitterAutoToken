from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
 
#创建浏览器对象
driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)#executable_path:浏览器驱动路径
driver.delete_all_cookies()
driver.get("https://mobile.twitter.com/Twitter")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(10)
data=driver.get_cookie('gt')
with open('/root/api/token.json','w',encoding='utf-8') as fp:
    json.dump(data,fp)
