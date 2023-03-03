FROM ubuntu
MAINTAINER metrics
LABEL app.maintainer=lqy
LABEL app.version="1.0" description="metrics test"
COPY ./Python-2.7.16.tgz /var/python2/Python-2.7.16.tgz
COPY ./time_series_detector/ /var/test/time_series_detector/
COPY ./test.py /var/test/test.py
RUN apt-get update\
&& apt-get install -y build-essential python2.7 curl \
&& ln -s /usr/bin/python2.7 /usr/bin/python \
&& curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py \
&& python get-pip.py\
&& ln -s /usr/bin/pip2 /usr/bin/pip \
&& pip install statsmodels==0.10.2 \
&& pip install scikit-learn \
&& pip install xgboost \
&& pip install tsfresh \
&& cd  /var/test/ \
&& python ./test.py 

