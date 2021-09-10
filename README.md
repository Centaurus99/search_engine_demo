# search_engine_demo

基于 Django 的程序设计训练课程作业

用于展示和搜索 [bilibili-spider](https://github.com/Centaurus99/bilibili-spider) 所爬取数据的简易搜索网站

编写时使用 `Python 3.8.7` + `Django 3.2.7`

## 致谢

- CSS 框架使用 [Semantic UI](https://github.com/semantic-org/semantic-ui)
- B站图标来自 [bili_icon_pack](https://github.com/dashuchufang/bili_icon_pack)

## 使用说明

### 开发

- 安装 `Django`：`pip3 install Django`

- 将爬虫爬取的数据库放置在项目根目录下，并命名为 `db.sqlite3`
- 运行 `python3 manage.py migrate` 生成数据库相关内容和索引
- 如果图片文件将部署在本地，则需要将爬虫爬取的 `data` 目录放置在 `Web` 项目的 `./searcher/static/searcher/` 目录下
- 运行 `python3 manage.py runserver` 即可开启开发服务器

### 部署

- 将 `./website/settings.py` 中的 `DEBUG` 选项改为 `False`

- 部署教程参考官方文档 [部署教程](https://docs.djangoproject.com/zh-hans/3.2/howto/deployment/) ，这里提供使用 `uwsgi` 和 `nginx` 进行部署的简要指引

- `pip3 install uwsgi` 安装 `uwsgi`

- 在项目根目录下新建 `uwsgi.ini` ，并作类似如下配置（仅供参考）：

- ```ini
  [uwsgi]
  chdir = 项目目录位置
  module = website.wsgi:application
  socket = 0.0.0.0:8000
  master = true
  buffer-size = 65536
  disable-logging = true

- `uwsgi uwsgi.ini` 即可开始运行服务器，可根据需要丢给 `systemctl` 管理

- 在 `nginx` 中进行类似如下配置：

- ```nginx
  server {
      listen 80;
          location / {
          include  uwsgi_params;
          uwsgi_pass  127.0.0.1:8000;
      }
      location /static {
          alias 项目目录/searcher/static;
      }
  }
  ```

- `sudo nginx -t` 检查，`sudo nginx -s reload` 重载配置

- 完成！

- 如果网页服务器和静态文件服务器分离，需要注意如果网页使用 `https` ，则静态文件服务器也需要使用 `https`

## 设计简介

- 后端部分
  - 模型层：使用 `SQLite` 数据库，无缝衔接 [bilibili-spider](https://github.com/Centaurus99/bilibili-spider) 所爬取数据，只对需要排序和单项选取的字段建立索引，查询速度满足需求
  - 视图层：基于 `Django` 的通用显示视图 `ListView` 和 `DetailView` 并进行了一定的改造，增加了相关查询计时和页面需要显示的信息
  - 模板层：根据 CSS 框架提供的 [教程](https://semantic-ui.com/introduction/getting-started.html) 进行页面和元素设计
- 前端部分使用 CSS 框架 [Semantic UI](https://github.com/semantic-org/semantic-ui) ，并编写了 `jump.js` 进行页码跳转的检验和页面跳转
