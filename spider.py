
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from urllib.request import urlretrieve
from createDoc import make_doc




class THREAD(QThread):
    _signal = pyqtSignal(str)
    def __init__(self,url,doc_name) -> None:
        super().__init__()
        opt = Options()
        opt.add_argument('--no-sandbox')                # 解决DevToolsActivePort文件不存在的报错
        opt.add_argument('--disable-gpu')               # 谷歌文档提到需要加上这个属性来规避bug
        opt.add_argument('blink-settings=imagesEnabled=false')      # 不加载图片，提升运行速度
        opt.add_argument('--headless')                  # 浏览器不提供可视化界面。Linux下如果系统不支持可视化不加这条会启动失败
        self.url = url
        self.doc_name = doc_name
        self.brower = webdriver.Chrome(options=opt)
        

    def run(self):

        images_folder_name = self.doc_name.split('.')[0]

        self.brower.get(self.url)
        
        doc = []

        title = self.brower.find_element_by_id('activity-name')
        publish_time = self.brower.find_element_by_id('publish_time')

        subtitles = self.brower.find_elements_by_tag_name('strong')
        contents = self.brower.find_elements_by_tag_name('span')
        images = self.brower.find_elements_by_class_name("wxw-img")
        if not os.path.exists(f'{images_folder_name}_images'):
            os.mkdir(f'./{images_folder_name}_images')

        for subtitle in subtitles:
            doc.append(['subtitle',subtitle.text,subtitle.location['y']])
        for content in contents:
            doc.append(['content',content.text,content.location['y']])
        for id,image in enumerate(images):
            img_url = image.get_attribute('data-src')
            img_name = f'./{images_folder_name}_images/{id}.png'
            urlretrieve(img_url, img_name)
            if image.size['height']>50 and image.size['width']>50:
                doc.append(['image',img_name,image.location['y']])
        
        doc.sort(key=lambda x:x[2])
        #print(doc)
        
        make_doc(title.text,publish_time.text,doc,self.doc_name)
            
        #url = "https://mp.weixin.qq.com/s/ZH1nU8I8lGoORYo8SLXS_w"
        #url = "https://mp.weixin.qq.com/s/kEmNwVk5DcacxPjLNxds8Q"
        
        print('finished')
        self._signal.emit("finish")

