# 图像几何变换 

# 一、目的
1. 了解图像增强的几何变换；
2. 学会图像的平移、缩放、旋转、镜像等几何运算。

# 二、内容
1. 编写程序，实现图像的缩放、旋转、镜像等几何变换。
2. 编写程序，实现图像的平移，要求两个平移量TX、TY可取正负值（TX、TY可用键盘输入），平移的功能用子函数实现。
3. 利用“二值图像与原图像做点乘,得到子图像”的原理.，编写M程序，构造特殊的二值图像，最终得到需要的子图像。

# 三、使用说明：
## 1. 创建画布
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2/img/01.png)
可自定义画布大小，点击确认完成画布创建。
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2/img/02.png)





## 2. 添加图像
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2/img/03.png)
选择一张图像点击打开；
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2/img/04.png)

## 3. 缩放
先点击左侧缩放按键
改变上方拉条修改想缩放的数值
点击确认完成缩放操作
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2/img/05.png)

 
## 4. 旋转
先点击左侧旋转按键
改变上方拉条修改想旋转的数值
点击确认完成缩放操作
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2/img/06.png)
 
 
## 5. 镜像
先点击左侧镜像按键
点击右上角选项完成镜像操作
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2/img/07.png)

 
## 6. 平移
先点击左侧平移按键
修改右上角数值完成平移操作，可以输入也可以点击按键，正负均可
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2/img/08.png)

 
## 7. 切割
点击左侧切割按键
在新窗口中可先调节画笔颜色粗细（彩色画笔最终会转化为灰度值）
在窗口中绘制，黑色区域会被遮罩进行覆盖
点击确认完成切割操作
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/%E5%9B%BE%E5%83%8F%E5%87%A0%E4%BD%95%E5%8F%98%E6%8D%A2/img/09.png)



