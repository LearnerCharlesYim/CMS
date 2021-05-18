from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)

class Cof(models.Model):
    name = models.CharField(max_length=100)#Cof名
    connection = models.CharField(max_length=100) #连接方式
    dimension = models.IntegerField()#理论维度
    author = models.ForeignKey('User',on_delete=models.CASCADE)

class Cofextension(models.Model):
    number = models.CharField(max_length=100)#编号
    acohnongdu = models.FloatField(null=True)#AcOH浓度
    acohliang = models.FloatField(null=True)#AcOH量
    temperature = models.FloatField()#温度
    time = models.IntegerField()#时间
    is_solid = models.BooleanField()#是否有固体
    is_crystal = models.BooleanField()#是否有晶体
    pxrd = models.IntegerField()#PXRD主峰高度

    ssnmr = models.FloatField(null=True)#ssnmr半峰宽
    hp129 = models.FloatField(null=True)#hp129Xe位移
    fengguan129 = models.FloatField(null=True)#封管129位移
    kongjing = models.FloatField(null=True)#孔径大小
    bet = models.FloatField(null=True)#BET比表面积
    graph = models.CharField(max_length=254,null=True)#理论结构图
    cif = models.CharField(max_length=254,null=True)#CIF文件
    graphpxrd = models.CharField(max_length=254,null=True)#pxrd图
    other = models.CharField(max_length=254 ,null=True)#其他文件
    remark = models.CharField(max_length=254,null=True)#备注

    cof = models.ForeignKey('Cof',on_delete=models.CASCADE)


class Danti(models.Model):
    danti = models.FloatField()#单体(mmol)
    name = models.CharField(max_length=100,null=True)#单体名称
    structure = models.CharField(max_length=254,null=True)#单体结构
    owner = models.ForeignKey('Cofextension',on_delete=models.CASCADE)

class Rongji(models.Model):
    name = models.CharField(max_length=100)#溶剂名称
    rongjiml = models.FloatField()#溶剂ml
    owner = models.ForeignKey('Cofextension',on_delete=models.CASCADE)

class Cuihuaji(models.Model):
    cas1 = models.CharField(max_length=100, null=True)  # 催化剂名称
    cas1liang = models.FloatField(null=True)  # 催化剂量
    owner = models.ForeignKey('Cofextension', on_delete=models.CASCADE)



