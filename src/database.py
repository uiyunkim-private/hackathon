import pymysql

def runsql(statement,param):
    db = pymysql.connect(host='hackathon.c41ospthg6le.us-east-2.rds.amazonaws.com',
                         port=3306,
                         user='umlkorean',
                         passwd='#wQy6IQY6v10Bp91cG^s8yJU!',
                         db='RAN',
                         charset='utf8')

    cursor = db.cursor()

    sql = statement

    cursor.execute(sql,param)
    cursor.execute("SHOW TABLES")

    db.commit()
    db.close()