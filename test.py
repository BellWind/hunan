#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json, MySQLdb

def CreateTable():
    try:
        conn = MySQLdb.Connect(
            host='111.205.121.93',
            user='user',
            passwd='g927@buaa',
            db='government',
            port=9002,
            )
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS `testdb`( \
            `id` INT(11) AUTO_INCREMENT,\
            `code` VARCHAR(15) NOT NULL,\
            `index` VARCHAR(4) NOT NULL,\
            `name` VARCHAR(255) NOT NULL,\
            `image_url` VARCHAR(255),\
            `profile` TEXT,\
            `organization` VARCHAR(255),\
            `position` VARCHAR(255),\
            PRIMARY KEY ( `id` )\
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;")
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# CreateTable()

def JsonToTable():
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

        data = []
        with open('xxgk.json') as f:
            for line in f:
                if(line[0] != "{"):
                    continue
                str = line.decode("GBK")
                str = str[0:len(str)-2]
                # print str
                tmp = json.loads(str, strict=False)
                data.append(tmp)

        cnt = 2
        id = 1
        for item in data:
            sql = "INSERT INTO officer(`id`,`code`,`index`,`name`,`profile`,`organization`,`position`) VALUES "
            sql = sql + "('%d','%s','%04d','%s','%s','%s','%s');\r\n" % (id,'430000',cnt,item['name'],item['resume'],item['dep'],item['duty'])
            cnt = cnt + 1
            id = id + 1
            cur.execute(sql)
            cur.nextset()

        cur.close()
        conn.commit()
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

JsonToTable()