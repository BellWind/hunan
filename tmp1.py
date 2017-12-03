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
    id = 779
    index = 780
    name = "王群"
    image_url = "http://ozwyjb3op.bkt.clouddn.com/430000_0780.jps"
    profile = r"王群，男，汉族，1961年6月生，湖南沅江人，1981年8月参加工作，1987年10月加入中国共产党，中央党校大学学历，工程师。现任省人民政府秘书长、党组成员，办公厅党组书记，常德市人大常委会主任。\
　　主要经历：1979年9月至1981年8月，铁道部田心铁路技术学校机械制造专业中专学习；1981年8月至1984年11月，株洲电力机车厂变压器分厂技术员、助理工程师；1984年11月至1988年1月，株洲电力机车厂办公室秘书、工程师；1988年1月至1996年2月，株洲电力机车厂办公室副主任、主任（1985年9月至1988年7月，中央党校经济管理专业函授专科学习）；1996年2月至2000年2月，株洲市人民政府副秘书长，政府办公室主任、党组副书记；2000年2月至2000年9月，株洲市石峰区委书记；2000年9月至2000年11月，株洲市委常委、石峰区委书记；2000年11月至2005年7月，株洲市委常委、株洲高新区党工委书记、天元区委书记（2000年8月至2002年12月，中央党校函授学院行政管理专业函授本科学习）；2005年7月至2006年12月，株洲市委常委、市纪委书记；2006年12月至2008年5月，株洲市委常委、市人民政府副市长（常务）；2008年5月至2009年1月，株洲市委副书记、市人民政府代市长；2009年1月至2013年3月，株洲市委副书记、市人民政府市长；2013年3月至2017年1月，常德市委书记；2017年1月至2017年3月，常德市委书记、市人大常委会主任；2017年3月至今，省人民政府秘书长、党组成员，办公厅党组书记，常德市人大常委会主任。"
    organization = "政府"
    position = "秘书长"
    sql = head + "('%d','%s','%04d','%s','%s','%s','%s','%s');" % (id,'430000',index,name,image_url,profile,organization,position)

    # print sql
    cur.execute(sql)
    cur.nextset()

    cur.close()
    conn.commit()
    conn.close()


except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])