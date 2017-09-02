# About Project
用python实现通过文件及目录创建、复制等操作，实现简单的项目打包、备份等

## Usage
```
配置:assets/config.json
read_path:指定读取文件目录
out_path:指定输出文件目录
create:[
    {
        name:创建的目录或文件路径,
        is_file:是否是文件(true/false),
        content:文件的话可制定初始化内容
    },
    ...]
copy:[
    {
        old_path:复制的目录或文件的源路径,
        new_path:复制的目录或文件的目标路径
    },
    ...]

执行:python scripts/main.py
```
## About Me
#### 博客: https://jay-y.github.io
#### 邮箱: 570440569@qq.com
