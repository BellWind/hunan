#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

try:
    conn = MySQLdb.Connect(
        host='111.205.121.93',
        user='user',
        passwd='g927@buaa',
        db='government',
        port=9002,
        charset="utf8"
    )
    cur = conn.cursor()

    head = "INSERT INTO officer(`id`,`code`,`index`,`name`,`image_url`,`profile`,`organization`,`position`) VALUES "
    id = 790
    index = 791
    name = "张能峰"
    image_url = "http://ozwyjb3op.bkt.clouddn.com/430100_0791.jps"
    profile = r"张能峰，男，汉族，1969年12月出生，湖南安乡人，1988年7月参加工作，中共党员，在职研究生学历。\
    学习经历\
    198509—198807 湖南省桃源师范学院师范专业学习\
    199109—199406 湖南省委党校行政管理专业学习\
    199908—200112 中央党校经济管理专业函授学习\
    200009—200306 湖南商学院经济管理专业函授学习\
    200609—200906 湖南师范大学政治学理论专业学习，在职研究生毕业，法学硕士\
    工作经历\
    198807—199008 湖南华南光电仪器厂子弟学校教师\
    199008—199108 湖南华南光电仪器厂团委组织干事\
    199108—199210 湖南华南光电仪器厂团委办公室主任\
    199210—199508 湖南华南光电仪器厂团委副书记\
    （其间：199411—199508共青团湖南省委组织部挂职锻炼）\
    199508—199602 共青团湖南省委宣传部干部\
    199602—199706 共青团湖南省委宣传部宣传教育科科长\
    199706—199805 共青团湖南省委办公室团刊编辑部主任\
    199805—199905 共青团湖南省委宣传部宣传教育科科长\
    199905—200105 共青团湖南省委青工部副部长\
    200105—200205 共青团湖南省委青工部部长\
    200205—200508 中共绥宁县委副书记（正处）\
    200508—200604 中共武冈市委副书记（正处）\
    200604—201204 中共邵阳市大祥区委副书记、政府区长\
    201204—201410 中共邵阳市大祥区委书记\
    （其间：201303—201306 湖南省委党校中青年干部培训班学习）\
    201410—201501 中共长沙市雨花区委副书记、政府代区长\
    201501—201607 中共长沙市雨花区委副书记、政府区长\
    201607—201701 长沙市人民政府副秘书长，长沙市政府办公厅党组副书记（正县）\
    201701—201702 长沙市人民政府党组成员，长沙市人民政府秘书长提名人选，长沙市人民政府办公厅党组书记\
    201702—      长沙市人民政府党组成员，长沙市人民政府秘书长，长沙市人民政府办公厅党组书记"
    organization = "市政府"
    position = "秘书长"
    sql = head + "('%d','%s','%04d','%s','%s','%s','%s','%s');" % (id,'430100',index,name,image_url,profile,organization,position)

    # print sql
    cur.execute(sql)
    cur.nextset()

    cur.close()
    conn.commit()
    conn.close()


except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])