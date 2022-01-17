

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from urllib.request import urlretrieve
from createDoc import make_doc


def main(url):
    browser.get(url)
    
    doc = []

    title = browser.find_element_by_id('activity-name')
    publish_time = browser.find_element_by_id('publish_time')

    subtitles = browser.find_elements_by_tag_name('strong')
    contents = browser.find_elements_by_tag_name('span')
    images = browser.find_elements_by_class_name("wxw-img")
    if not os.path.exists('images'):
        os.mkdir('./images')

    for subtitle in subtitles:
        doc.append(['subtitle',subtitle.text,subtitle.location['y']])
    for content in contents:
        doc.append(['content',content.text,content.location['y']])
    for id,image in enumerate(images):
        img_url = image.get_attribute('data-src')
        img_name = f'./images/{id}.png'
        urlretrieve(img_url, img_name)
        if image.size['height']>50 and image.size['width']>50:
            doc.append(['image',img_name,image.location['y']])
    
    print('get all pictures')
    doc.sort(key=lambda x:x[2])
    #print(doc)
    
    return title.text,publish_time.text,doc


        

if __name__ == '__main__':
    url = "https://mp.weixin.qq.com/s/kEmNwVk5DcacxPjLNxds8Q"
    opt = Options()
    opt.add_argument('--no-sandbox')                # 解决DevToolsActivePort文件不存在的报错
    opt.add_argument('--disable-gpu')               # 谷歌文档提到需要加上这个属性来规避bug
    opt.add_argument('blink-settings=imagesEnabled=false')      # 不加载图片，提升运行速度
    opt.add_argument('--headless')                  # 浏览器不提供可视化界面。Linux下如果系统不支持可视化不加这条会启动失败

    browser = webdriver.Chrome(options=opt)

    title,publish_time,doc = main(url)
    make_doc(title,publish_time,doc)