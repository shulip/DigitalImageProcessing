# 灰度映射
---

# 一、目的
1. 了解图像的灰度映射；
2. 实现图像的点运算和灰度拉伸；
3. 掌握直方图均衡化处理。

# 二、内容
1. 在GUI中，实现图像的点运算（G=aF+b），要求有灵活的a、b参数选择。
2. 在GUI中，实现图像的灰度拉伸，要求有灵活的（a,a’）点、（b,b’）点的选择。
3. 在GUI中，实现图像的直方图均衡化。
4. 第1、2题，用曲线控件完成。

 
# 三、实验代码及实验结果截图
    
## 1. 线性变换
令F为变换前的灰度，G为变换后的灰度，则线性变换函数为：
$G=aF+b$
其中a为直线斜率，b为y轴上截距。由于灰度图像中灰度值范围为[0,255]，因此超过此范围的取边缘值。

当a=1.2，b=60时，函数如下图所示：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/01.png)


 
## 2. 线性变换变体
此为折线函数，仅添加了点进行分段，原理相同不多做概述。

取一些点，函数如下图所示：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/02.png)

 
## 3. 直方图均衡化
下图显示原图像及其灰度直方图，变换后图像及其灰度直方图，及其变换函数：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/03.png)

 
## 4. 多项式函数

形如$f(x)=a_n\ x^n+a_(n-1)\ x^(n-1)+\cdots+a_2\ x^2+a_1\ x^1+a_0$的函数为多项式函数。多项式函数系数可根据n点式进行计算，例如二次函数可根据三点式计算出函数方程：
假设有三点$(x_1,y_1) (x_2,y_2)(x_3,y_3)$,则二次函数方程为
$f(x)=((x-x_2)∙(x-x_3))/((x_1-x_2)∙(x_1-x_3))×y_1+((x-x_1)∙(x-x_3))/((x_2-x_1)∙(x_2-x_3))×y_2+((x-x_1)∙(x-x_2))/((x_3-x_1)∙(x_3-x_2))×y_3$  
同理可得多项式函数：
$f(x)=((x-x_2)∙(x-x_3)⋯(x-x_n))/((x_1-x_2)∙(x_1-x_3)⋯(x_1-x_n))×y_1+⋯+((x-x_1)∙(x-x_2)⋯(x-x_(n-1)))/((x_n-x_1)∙(x_n-x_2)⋯(x_n-x_(n-1)))×y_n$
由于灰度图像中灰度值范围为$[0,255]$，因此超过此范围的取边缘值。

取一些点，函数如下图所示：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/04.png)
伽马变换：
令F为变换前的灰度，G为变换后的灰度，伽马变换的公式为：
$G=cF^γ$
其中$c$和$γ$为正常数。伽马变换的效果与对数变换有点类似，当$γ>1$时将较窄范围的低灰度值映射为较宽范围的灰度值，同时将较宽范围的高灰度值映射为较窄范围的灰度值；当$γ<1$时，情况相反，与反对数变换类似。其函数曲线如下：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/05.png)

 
# 使用说明:
点击文件，选择一张图片打开，接着选择上方按钮：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/06.png)
点击线性按钮后，通过改变下方拉条进行改变灰度映射：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/07.png)

点击折线按钮后，可以改变曲线视图内的点或是添加点，根据鼠标所点位置自动判断：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/08.png)

点击曲线按钮后，可以改变曲线视图内的点或是添加点，根据鼠标所点位置自动判断：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/09.png)


点击直方图均衡化后直接进行显示：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/10.png)
点击伽马变换，通过修改下方gamma值进行修改灰度映射：
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/04%E7%81%B0%E5%BA%A6%E6%98%A0%E5%B0%84/img/11.png)