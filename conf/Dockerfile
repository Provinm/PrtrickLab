FROM python:3.7

WORKDIR /server

ADD ../requirements.txt /server/

# RUN pip install git+https://github.com/Supervisor/supervisor
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# USER ebrose

EXPOSE 80 8000 443

CMD ["uwsgi", "--ini", "/server/PatrickLab/conf/lab.conf"]