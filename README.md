# myGraduationProject

## 目录结构
| 目录 | 功能 |
| --- | --- |
|/deploy/ | prometheus + grafana环境 | 
|/prophet/ | prophet算法目录 |
|/python_env_image/ | python环境镜像文件 |
|/metrics_image/ | metrics_image环境镜像文件 |
|/metrics_image/time_series_detector/ | metrics算法目录 |
|/metrics_image/test.py | metrics算法测试文件 |

## 关于prometheus环境
    请查看/deploy/,并按照readme中顺序执行yaml文件
## 关于docker
  有两个镜像
- python环境镜像```docker build -t python_env:1.0 ./python_env_image/.```
- metrics镜像
```docker build -t metrics:1.0 ./metrics_image/.```