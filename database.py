from table import Table, Row, Field
from typing import Tuple

class Database:
    def __init__(self, database_name:str):
        self.database_name = database_name
        self.tables: list[Table] = list()

    def add_table(self, field_descriptions: list[Tuple[str,str]], name: str) -> Table:
        table = Table(name=name)
        for field in field_descriptions:
            name, field_type = field
            table.add_field(Field(name=name, field_type=field_type))
            self.tables.append(table)
            return table

    def __str__(self) -> str:
        return f"Tables: {self.database_name}, {len(self.tables)} tables"

    def get_tables(self) -> list[Table]:
        return self.tables