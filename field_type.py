class FieldType:
    def __init__(self, name:str):
        self.name = name

    def __str__(self) -> str:
        return f"Field: {self:name}"