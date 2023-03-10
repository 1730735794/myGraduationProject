FROM ubuntu
MAINTAINER python
LABEL app.maintainer=lqy
LABEL app.version="1.0" description="python env"
RUN apt-get update\
&& apt-get install -y build-essential python2.7 curl \
&& ln -s /usr/bin/python2.7 /usr/bin/python \
&& curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py \
&& python get-pip.py\
&& rm -f get-pip.py

