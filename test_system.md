# 作业提交与批改系统
Homework submission and grading

概述:
作业提交与批改系统是为学生与教师之间提供在线答题和作业提交批改的平台,任课老师在系统上可组织作业题库,将作业指派给学生,系统通过试题库实现自动批改的任务.学上端可以查看最新的作业,查看完成进度,提交状态,成绩等功能

1.登录/注册

​	学生:只能使用登录功能,学生由超级管理员或老师进行注册

​	老师:可以实现学生注册和 自身的登录

​	superuser:老师和学生注册,班级的创建等,可操纵所有数据库





2.学生登录后功能
	1>作业提交与批改
		学生要完成老师指定数量的题目,学生完成后提交后台自动批改并计时
		批改后学生可查看成绩 历史试题 正确答案
	2>错题本功能,学生可查看历史错题,或者添加错题
	3>考试历史:可查看历史成绩 历史试题
	4>个人资料修改:头像 昵称 年龄 等修改
	5>云笔记
	** 在线答疑



3 教师登录后功能
 	1.添加/修改/删除试 题库 
 	2.组卷可自动组卷和手动组卷 分发作业,规定完成时间
 	3.查看学生完成情况和成绩,学生成绩分析
  	4.查看具体学生的答题情况
	**在线答疑



4.管理员

管理员登录界面

权限管理

信息修改





## 一.开发环境

ubuntu 16.04   python 3.6  Django 1.11.8   AJAX   JSON   mysql



## 二 功能设计

![项目功能设计](/home/tarena/下载/项目功能设计.jpg)



### 1.数据库

创建 Homework数据库

```mysql
create database homework
```

### 2.数据表设计

1)表名: studs

表结构:

​		name: varchar(16) 学生姓名

​		stuid:  int 学号 主键

​		classid:班级编号 foreign classid

​		school: varchar(32):学校

​		college: vachar(32):学院	

​		major:varchar(32) 专业

​		email:varchar(32)

​		regdate:date 注册日期

​	password:varchar(32)

2) 表名:teacs:教师

​	表结构: 

​			teaid: int 教师编号 主键

​			name:varchar(16)

​			email:varchar(32)

​			password:varchar(32)

​			regdate:date 注册日期

3) 表名:class  存储班级信息

​		表结构:

​			classid :int 班级编号 主键

​			classname:班级名称 not null

​			teaid: int 外键 teacs.teaid

​			createdate:date 开班日期

4) 表名:subjs:科目表

表结构:

subid : int :科目ID 主键

subname:科目名称

5)表名:quess:试题库

qid:int 试题ID

ques:text 试题内容

choise1: text

choise2

choise3:

choise4:

answer:  choise1/choise2/

explain:text

subid:科目 外键 subjs.subid

ceratedata:date 试题上传时间

6)表名:papers:试卷库



​	papid:int 试卷ID 主键

​	title:varchar(32):作业标题

​	createdate:data 创建时间

​	subid: 科目 外键 subjs.subid

​	number:int 试题总数



7)表名:papque:试卷试题对照表  多对多

​	papid:int 试卷ID 外键 papers.papid

​	qid: int 试题ID 外键 quess.qid



8.表名:testinf:考试信息表

​		papid : 试卷ID  外键 papers.papid

​		classid: 考试班级ID 外键 class.classid

​		startime:datetime 作业开始时间

​		duration:int  考试时长  秒

​		deadline:datetime 作业最后提交时间

​		statues:BOOL 信息状态



9.表名:history: 作业历史

​	hisid :int 主键

​	stuid: 外键 学生学号 studs.stuid

​	papid:试卷ID 外键 papers.papid

​	grade: decimal(4,1) 成绩

​    status: 完成状态 BOOL (TRUE 已完成 FALSE 未完成)

  submitime:datatime:提交时间

10.表名:topic:错题

​	hisid:历史ID 外键 history.hisid

​	qid:试题ID 外键quess.qid

​	answer:varchar(16) 学生答案

11. 表名 managers:

    manaid:int  管理员ID 

    manager: varchar(16) 管理员姓名 unique

    pasword:varchar(32)

     permission: small int  管理权限  使用四位二进制,表示最低位表示更改或添加学生信息的权限 ,第二位表示更改或添加老师的权限 ,第三位 表示添加和删除管理员的权限 第四位表示课程管理班级的权限  1表示具有该权限 0表示不具有该权限,例如:b1111 表示具有最高权限 b0001表示只能修改增删使用学生信息  0000表示只能查阅 

    
    
    

`登录功能`

   	实现学生/老师的登录:要求若学生或老师未登录则 提示 ,登陆后跳转到个人主页

​		管理员用户由专用页面登录

`老师个人主页:`

1 可实现手动组卷,自动组卷, 试卷展示

2 添加/删除题库,

3 发起考试,

4 查看学生成绩,作业完成程度

5 可扩展:在线答疑 资料推送

`学生个人主页:`

1 可实现个人资料修改 ,

2 参加考试 

3 查看考试成绩

4 考试历史 

5 查看具体考试试卷 

6 自动和手动添加错题本.

7 可扩展: 云笔记 在线答疑 资料下载

`superuser:`

1>用户管理

2>  科目班级创建  

3> 管理员用户创建 及权限管理

管理员用户登录后根据其权限显示对应的功能,不可操作内容不显示

管理权限  使用四位二进制,表示最低位表示更改或添加学生信息的权限 ,第二位表示更改或添加老师的权限 ,第三位 表示添加和删除管理员的权限 第四位表示课程管理班级的权限  1表示具有该权限 0表示不具有该权限,例如:b1111 表示具有最高权限 b001表示只能修改增删使用学生信息  

****

模块设计:



![模块设计](/home/tarena/下载/模块设计.jpg)

managerModelViewSet.py

* add_manager(permission,managername):

  返回值:管理员已存在返回false 创建成功返回True

  参数: 权限,管理员名称

* del_manager(managername):

  返回值:True / False

  参数: 管理员名称

* add_student(stuid,stuname,classid,school,college,major,email=None)

添加学生

返回值Ture/False



具体实现犯法即返回值 参数请自行补充

​	

github远程仓库使用

多个人负责一个模块

student teacher  manager三个branch

```
git remote  add Student https://github.com/LICKJIA/exam_system.git
```







