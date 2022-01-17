# WeChat official account spider

## Show

Wechat pages

![image-20220117163115159](https://raw.githubusercontent.com/learner-lu/picbed/master/image-20220117163115159.png) 

Word 

![image-20220117163258944](https://raw.githubusercontent.com/learner-lu/picbed/master/image-20220117163258944.png) 


## Requirement
- selenium [Tutorial blog](https://blog.csdn.net/weixin_36279318/article/details/79475388)
  ```shell
  pip install selenium
  ```
  [blog to install](https://www.cnblogs.com/lfri/p/10542797.html)
  check your Google browser's version, choose the closest version and download corresponding GoogleDriver from [position1](http://chromedriver.storage.googleapis.com/index.html) or [position2](https://npm.taobao.org/mirrors/chromedriver/).And then move `chromedriver.exe` under `C:\Program Files\Google\Chrome\Application` and the same folder with your python explainer. Then add `C:\Program Files\Google\Chrome\Application` to your `system path`.

- docx [Main usage blog](https://www.cnblogs.com/gdjlc/p/11407587.html)
  ```shell
  pip install python-docx
  ```
- urllib 
  ```shell
  pip install urllib3
  ```

## Use 
```shell
python spider.py
```
All the images will be downloaded under folder `./images` and a word document will be created as `paper.docx`

## Attention

As far as I know, spiders often need to read the Web page source code and find the targeted labels and then do some jobs. So **this code is not a general Wechat spider which can get all WeChat official account articles**, if you have interests you should write your own spider for your targeted Web pages.

