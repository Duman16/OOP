from field import Field
from row import  Row
def test_field():
    field1 = Field(name="id", field_type="int")
    assert isinstance(field1, Field)
    assert field1.name == "id"
    assert field1.field_type == "int"


def test_create_row():
    id_ = Field(name="id", field_type="int")
    name = Field(name="name", field_type="str")

    row1 = Row(
        data = {
            "id": 1,
            "name": "Duman",
        },
        fields = [
        id_,
        name,
    ]
    )
    row2 = Row(
        data={
            "id": 2,
            "name": "Temirlan",
        },
        fields=[
            id_,
            name,
        ]
    )
    row3 = Row(
        data={
            "id": 3,
            "name": "Tair",
        },
        fields=[
            id_,
            name,
        ]
    )
    assert isinstance(row1, Row)
    assert isinstance(row2, Row)
    assert isinstance(row3, Row)
    assert row1["id"] == 1
    assert row1["name"] == "Duman"
    assert row2["id"] == 2
    assert row2["name"] == "Temirlan"
    assert row3["id"] == 3
    assert row3["name"] == "Tair"