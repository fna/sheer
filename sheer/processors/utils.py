import MySQLdb
import os


def run_query(query):
    host = os.environ.get('SHEER_DBHOST', 'localhost')
    user = os.environ.get('SHEER_DBUSER', 'root')
    passwd = os.environ.get('SHEER_DBPASS', '')
    db = os.environ.get('SHEER_DATABASE', 'sheer')

    try:
        print query
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        cur = db.cursor()
        cur.execute(query)
        columns = [column[0] for column in cur.description]
        results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
        return {'results': results}
    except Exception as e:
        return {'error': e}
