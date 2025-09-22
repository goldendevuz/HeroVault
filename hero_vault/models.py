from finesql import Table, Column

class Hero(Table):
    name = Column(str)
    secret_name = Column(str)
    age = Column(int, default=None)  # Optional field
