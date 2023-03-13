FROM python:2.7

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 拷贝文件
ADD . /code/
WORKDIR /code

# 安装依赖
RUN python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip \
    && pip install -r requirements.txt 

CMD ["python","./metis.py"] 