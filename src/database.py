import pymysql

db = pymysql.connect(host='sql313.epizy.com',
                     port=3306,
                     user='epiz_26589997',
                     passwd='EwZ25pT5vjS08',
                     db='epiz_26589997_XXX',
                     charset='utf8')


cursor = db.cursor()

sql = """
    select * from (
           id INT UNSIGNED NOT NULL AUTO_INCREMENT,
           name VARCHAR(20) NOT NULL,
           model_num VARCHAR(10) NOT NULL,
           model_type VARCHAR(10) NOT NULL,
           PRIMARY KEY(id)
    );
    """

# sql = """
#     CREATE TABLE korea (
#            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
#            name VARCHAR(20) NOT NULL,
#            model_num VARCHAR(10) NOT NULL,
#            model_type VARCHAR(10) NOT NULL,
#            PRIMARY KEY(id)
#     );
#     """

cursor.execute(sql)
cursor.execute("SHOW TABLES")


db.commit()


db.close()