本项目为本人毕设项目，仅供学习，请勿直接抄袭，如有疑问可直接联系作者。详细介绍请访问CSDN：https://blog.csdn.net/jiqiu12/article/details/140017540
其中项目包为KG-VAQSystemOnMedical-master.zip直接下载即可，json数据集较大，存放在另一个名为“data”的branch中，不要忘了下载。
数据集下载完毕后直接放置KG-VAQSystemOnMedical-master文件目录下即可。
![image](https://github.com/jiqiu123/KG-VAQSystemOnMedical-master/assets/115466479/dc11f873-1d76-4977-9261-d039730009c5)
运行前，确保Neo4j数据库已安装并配置好环境，python中所需包也安装完毕。环境配置好后，先运行build_medicalgraph.py文件将数据入库并生成知识图谱，导入过程可能较久请耐心等待，如果想加快速度也可以删除一些数据集即可。
成功后，直接运行start.py然后进入网页输入网址：http://127.0.0.1:5000 即可跳转。

主页面：
![image](https://github.com/jiqiu123/KG-VAQSystemOnMedical-master/assets/115466479/d66c1092-4ad3-4e87-bd0e-4b892e10376d)
智能医疗小助手界面：
![image](https://github.com/jiqiu123/KG-VAQSystemOnMedical-master/assets/115466479/ee008da8-9add-4d4a-a55b-5234d1ab560d)
知识图谱可视化界面：
![image](https://github.com/jiqiu123/KG-VAQSystemOnMedical-master/assets/115466479/4e00675f-53d6-456b-ae6c-94c8776b30d4)
