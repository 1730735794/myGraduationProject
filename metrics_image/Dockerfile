FROM python_env:1.0
MAINTAINER metrics
LABEL app.maintainer=lqy
LABEL app.version="1.0" description="metrics test"
COPY ./time_series_detector/ /var/test/time_series_detector/
COPY ./test.py /var/test/test.py
RUN ln -s /usr/bin/pip2 /usr/bin/pip \
&& pip install statsmodels==0.10.2 -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
&& pip install scikit-learn -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
&& pip install xgboost -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
&& pip install tsfresh -i https://pypi.tuna.tsinghua.edu.cn/simple/ 

CMD python var/test/test.py -i 5