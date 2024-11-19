FROM python:3.10-bullseye
# 开放端口
EXPOSE 4455
# 定义运行目录
WORKDIR /app
# 复制当前根目录文件至镜像/app目录内
COPY . /app
# 执行安装依赖包命令
RUN pip install --no-cache-dir -r /app/requirements.txt

