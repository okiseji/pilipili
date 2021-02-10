import requests
import time
from selenium import webdriver
import random
from PIL import Image
import pytesseract
import builtins
from aip import AipOcr

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def image2text(fileName):
    image = get_file_content(fileName)
    dic_result = client.numbers(image)
    res = dic_result['words_result']
    result = ''
    for m in res:
        result = result + str(m['words'])
    return result
def get_html(url):
    try:
        # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        # kv={"usm":"3","rsv_idx":"2","rsv_page":"1"}
        r = requests.get(url, timeout=30)
        proxies = {
            'http': 'socks5://127.0.0.1:10808',
            'https': 'socks5://127.0.0.1:10808'
        }
        # r = requests.get(url, timeout=30,proxies=proxies)
        r.raise_for_status()
        r.encoding = 'utf-8'
        # print(r.text)
        return r.text
    except:
        return " ERROR "
def name():
    c=""
    words=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz")
    for i in range(0,8):
        r=random.randint(0,61)
        c+=words[r]
    print(c)
    return c
if __name__ == '__main__':
    APP_ID = '22055628'
    API_KEY = 'Ia2homkcCGGVikSrwX4hGR91'
    SECRET_KEY = '0W02byqO2fYF9juqklGZUqqhhRZpbSf1'
    '''
    这里写你滴邀请注册链接
    '''
    url="http://www.pilipili.cm/index.php/user/reg.html?uid=67307"
    '''
    这里写你滴邀请访问链接
    '''
    url2=""
    while 1:
        get_html(url2)
        time.sleep(1)
    while 1:
        options = webdriver.ChromeOptions()
        # proxy = '127.0.0.1:10808'
        # options.add_argument('--proxy-server=socks5://' + proxy)
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        username=name()
        driver.find_element_by_xpath('//*[@id="user_name"]').send_keys(username)
        password=name()
        driver.find_element_by_xpath('//*[@id="user_pwd"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="user_pwd2"]').send_keys(password)
        driver.save_screenshot('capture.png')
        ele = driver.find_element_by_xpath('//*[@id="verify_img"]')
        ele.screenshot('ele.png')
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        result = image2text('ele.png')
        print(result)
        driver.find_element_by_xpath('//*[@id="verify"]').send_keys(result)
        driver.find_element_by_xpath('//*[@id="btn_submit"]').click()
        driver.quit()



    # original_open = open
    # img = Image.open('ele.png')
    # try:
    #     builtins.open = bin_open
    #     bts = pytesseract.image_to_string(img)
    # finally:
    #     builtins.open = original_open
    # print(str(bts, 'cp1252', 'ignore'))







    # while 1:
    #     # time.sleep(1)
    #     options = webdriver.ChromeOptions()
    #     proxy = '127.0.0.1:10808'
    #     options.add_argument('--proxy-server=socks5://' + proxy)
    #     driver = webdriver.Chrome(options=options)
    #     driver.get(url)
    #     text = driver.find_element_by_xpath('/html/body/pre').text
    #     print(text[-7:-2])
    #     driver.quit()