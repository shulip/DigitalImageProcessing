# 图像变换 
----

# 一、目的
1. 了解图像从空域到频域的变换过程；
2.  实现傅里叶变换及离散余弦变换。
# 二、内容
1. 制作自己的 GUI用户界面，实现图像的傅里叶变换，并验证傅里叶变换的“平移不变性”、“旋转一致性”；
2. 用程序实现图像的离散余弦变换；
3. 模仿书P41的例4-4，利用傅里叶变换的模板匹配，实现在一个文本图像里的某个字母（如：字母a）的文本定位。

# 三、结果截图
## 1．

 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/01.png)

旋转一致性：
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/02.png)
平移不变性：
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/03.png)


## 2．
 ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/04.png)
 
## 3．
这里除去书上方法，还调用了opencv中的三种方法
结果：
书上
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/05.png)
 
平方差匹配：
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/06.png)
相关匹配：
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/07.png)
 
相关系数匹配：
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/08.png)


# 使用说明：
## 1. 首先导入图像
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/09.png)
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/10.png)
由于右上角为傅里叶变换，所以目前为傅里叶变换。
## 2. 点击左侧按钮“旋转”，拉动上方拉条即可完成旋转，实时傅里叶变换
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/11.png)
## 3. 点击左侧按钮“平移”，拉动上方拉条即可完成平移，实时傅里叶变换
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/12.png)
## 4. 点击右上方选择框改选离散余弦变换完成操作
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/13.png)
## 5. 点击左侧“模板匹配”，在点击上方匹配定位添加文件
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/14.png)
分别添加原图像和模板图像
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/15.png)
 
## 6. 先选择右上方不同的匹配算法，再点击左上方“执行”按钮完成匹配
  ![image](https://github.com/shulip/DigitalImageProcessing/blob/master/03%E5%9B%BE%E5%83%8F%E5%8F%98%E6%8D%A2/img/16.png)