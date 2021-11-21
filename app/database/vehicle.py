from app.database import get_db


def output_formatter(results:tuple):
    out = []
    for result in results:
        result_dict = {}
        result_dict["id"] = result [0]
        result_dict["license_plate"] = result [1]
        result_dict["v_type"] = result [2]
        result_dict["color"] = result [3]
        result_dict["parking_spot_no"] = result [4]
        result_dict["user_id"] = result [5]
        result_dict["discription"] = result [6]
        out.append(result_dict)
    return out


def insert( license_plate, v_type, color, parking_spot_no, user_id, discription, active=1):
    value_tuple = ( license_plate, v_type, color, parking_spot_no, user_id, discription)
    query = """
        INSERT INTO user (
            license_plate,
            v_type,
            color,
            parking_spot_no,
            user_id,
            discription
        ) VALUES (
            ?, ?, ?, ?, ?, ?
        )
    """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id
    


def scan():
    cursor = get_db().execute("SELECT * FROM user", () )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def read (pk):
    cursor = get_db().execute(
        "SELECT * FROM user WHERE active=1", (pk,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def update(pk, first_name, last_name, hobbies):
    value_tuple = (first_name, last_name, hobbies,)
    query = """
        UPDATE user
        SET first_name='%s',
        last_name='%s',
        hobbies='%s',
        WHERE id =?
    """ % (first_name, last_name, hobbies)

    cursor = get_db()
    cursor.execute(query, value_tuple)
    cursor.commit()
    cursor.close()


def deactive_user(pk):
    cursor = get_db()
    cursor.execute(
        "UPDATE user SET active=0 WHERE id=?", (pk,))
    cursor.commit()
    cursor.close