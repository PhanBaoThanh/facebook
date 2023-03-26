import sqlite3
from sqlite3 import Error
from app.modelView import BaiDangView

def test():
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    return 'ok'

def GetAllBaiDangCaNhan(manguoidung):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    print("Connected to SQLite")
    
    cursor.execute("select * from ViewBaiDangCaNhan\ where BaiDangCaNhan.MaNguoiDung = ?",(manguoidung))
    records = cursor.fetchall()
    list1 = []
    for row in records:
        list1.append(BaiDangView(MaBaiDang = row[0],MaNhom=None,MaNguoiDung=row[1],ThoiGianDang=row[2],NoiDung=row[3],Anh=row[4],IsNhom=False).serialize())
    
    cursor.close()
    return list

def GetAllBaiDangCaNhanByMaNguoiDung(manguoidung):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute("select * from ViewBaiDangCaNhan where BaiDangCaNhan.MaNguoiDung = ?",(manguoidung))
    records = cursor.fetchall()
    list1 = []
    for row in records:
        list1.append(BaiDangView(MaBaiDang = row[0],MaNhom=None,MaNguoiDung=row[1],ThoiGianDang=row[2],NoiDung=row[3],Anh=row[4],IsNhom=False).serialize())
    
    cursor.execute("select * from ViewBaiDangNhom where BaiDangNhom.MaNguoiDung = ?",(manguoidung))
    records = cursor.fetchall()
    list2 = []
    for row in records:
        list2.append(BaiDangView(MaBaiDang = row[0],MaNhom=row[1],MaNguoiDung=row[2],ThoiGianDang=row[3],NoiDung=row[4],Anh=row[5],IsNhom=True).serialize())
    
    list = list1 + list2
    list.sort(key = lambda x:x['ThoiGianDang'])
    
    cursor.close()
    return list
    
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    # cur.execute("SELECT * FROM tasks")
    cur.execute("select * from ViewBaiDangCaNhan")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = "D:\app\VisualStudioCode\workspace\Facebook\server\app.db"
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn, 1)

        print("2. Query all tasks")
        select_all_tasks(conn)


if __name__ == '__main__':
    main()