from typing import Any
from row import Row, Field
class Table:
    def __init__(self, name:str):
        self.name = name
        self.fields: list[Field] = list()
        self.rows: list[Row] = list()

    def add_field(self, field: Field):
        self.fields.append(field)

    def remove_field(self, field: Field):
        self.fields.remove(field)

    def get_fields(self):
        return  self.fields

    def get_rows(self) -> list[Row]:
        return self.rows

    def _insert_row(self, row: Row):
        self.rows.append(row)

    def insert(self, data: dict[str, Any]):
        new_row = Row(
            data=data,
            fields=self.fields
        )
        self._insert_row(new_row)