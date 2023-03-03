# AttributeError: 'module' object has no attribute '__version__'
statsmodels 0.11版本及以下(推荐0.10.2)
```
pip2 install statsmodels==0.10.2
```
requirment
```
Requirement already satisfied: scipy>=0.18 in /usr/local/lib/python2.7/site-packages (from statsmodels==0.10.2) (1.2.3)
Requirement already satisfied: numpy>=1.11 in /usr/local/lib/python2.7/site-packages (from statsmodels==0.10.2) (1.16.6)
Requirement already satisfied: pandas>=0.19 in /usr/local/lib/python2.7/site-packages (from statsmodels==0.10.2) (0.23.4)
Requirement already satisfied: patsy>=0.4.0 in /usr/local/lib/python2.7/site-packages (from statsmodels==0.10.2) (0.5.3)
Requirement already satisfied: python-dateutil>=2.5.0 in /usr/local/lib/python2.7/site-packages (from pandas>=0.19->statsmodels==0.10.2) (2.8.2)
Requirement already satisfied: pytz>=2011k in /usr/local/lib/python2.7/site-packages (from pandas>=0.19->statsmodels==0.10.2) (2022.7.1)
Requirement already satisfied: six in /usr/local/lib/python2.7/site-packages (from patsy>=0.4.0->statsmodels==0.10.2) (1.16.0)
```

# delaying package configuration, since apt-utils is not installed

此warning对结果没有影响，只影响交互式安装

# ImportError: No module named sklearn.ensemble

pip install scikit-learn
