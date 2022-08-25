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

  检查您的 Google 浏览器版本，选择最接近的版本并从以下位置下载对应的 chromedriver
  
  - [地址1](http://chromedriver.storage.googleapis.com/index.html)
  - [地址2](https://npm.taobao.org/mirrors/chromedriver/)

  复制`chromedriver.exe`到`C:\Program Files\Google\Chrome\Application`,并且将`C:\Program Files\Google\Chrome\Application`添加到环境变量

  打开控制台输入,提示 ChromeDriver was started successfully 则成功

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
