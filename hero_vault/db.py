import os
from finesql import Database
from icecream import ic

DB_PATH = "hero_vault.db"

class HeroVaultDB:
    def __init__(self, db_path=DB_PATH, reset=False):
        if reset and os.path.exists(db_path):
            os.remove(db_path)
        self.engine = Database(db_path)

    def create_table(self, table):
        self.engine.create(table)

    def save(self, instance):
        self.engine.save(instance)

    def all(self, table):
        return self.engine.all(table)

    def get(self, table, **filters):
        return self.engine.get(table, **filters)
