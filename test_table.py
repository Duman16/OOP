from table import Table, Row, Field
from database import   Database

def test_table():


    db = Database(database_name="AlmaU")
    students = db.add_table(field_descriptions=[("id_", "int"), ("name", "str") ], name="students")

    students.insert({"id": 1, "name": "Duman",})
    students.insert({"id": 2, "name": "Temirlan",})
    students.insert({"id": 3, "name": "Tair",})

    rows = students.get_rows()
    assert len(rows) == 3
    assert rows[0]["id"] == 1
    assert rows[0]["name"] == "Duman"
    assert rows[1]["id"] == 2
    assert rows[1]["name"] == "Temirlan"
    assert rows[2]["id"] == 3
    assert rows[2]["name"] == "Tair"

