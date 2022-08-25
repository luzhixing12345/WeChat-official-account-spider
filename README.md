# WeChat official account spider

微信公众号爬虫

## Result

Wechat pages

![image-20220117163115159](https://raw.githubusercontent.com/learner-lu/picbed/master/image-20220117163115159.png)

Word

![image-20220117163258944](https://raw.githubusercontent.com/learner-lu/picbed/master/image-20220117163258944.png)

## Requirement

- 安装依赖

  ```bash
  pip install -r requirements.txt
  ```

- 安装chromedriver

  > [安装教程1](https://www.cnblogs.com/lfri/p/10542797.html)
  >
  > [安装教程2](https://blog.csdn.net/weixin_36279318/article/details/79475388)

  1. 下载[谷歌浏览器](https://www.google.com/intl/zh-CN/chrome/)
  2. 检查您的 Google 浏览器版本，在浏览器中输入chrome://version/
  3. 选择最接近的版本并从以下位置下载对应的 chromedriver

     请注意版本选择时,若当前版本为`104.0.5112.101`, 104.0.5112.79 < 104.0.5112.101 < 105.0.5195.19,选择低于当前版本的最接近的104.0.5112.79下载
  
     - [地址1](http://chromedriver.storage.googleapis.com/index.html)
     - [地址2](https://npm.taobao.org/mirrors/chromedriver/)

  4. 解压后复制`chromedriver.exe`到`C:\Program Files\Google\Chrome\Application`,并且将`C:\Program Files\Google\Chrome\Application`添加到环境变量

  5. 打开控制台输入,提示 ChromeDriver was started successfully 则成功

     ```bash
     chromedriver
     ```

## Use

```shell
python GUI.py
```

![image-20220121235656098](https://raw.githubusercontent.com/learner-lu/picbed/master/image-20220121235656098.png)

## FAQ

如果运行发现一大堆看不懂的命令行报错,请先检查selenium是否成功运行,执行

```bash
python test.py
```

如果成功使用谷歌浏览器打开百度网页说明成功,否则检查上方chromedriver配置过程
