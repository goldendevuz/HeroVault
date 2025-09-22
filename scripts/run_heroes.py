from hero_vault.models import Hero
from hero_vault.db import HeroVaultDB
from icecream import ic

# Initialize database (reset=True clears previous DB)
db = HeroVaultDB(reset=True)
db.create_table(Hero)

# Hero instances
heroes_list = [
    Hero(name="Dead Pond", secret_name="Dive Wilson"),
    Hero(name="Spider-Boy", secret_name="Pedro Parquetry"),
    Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
]

# Save heroes
for hero in heroes_list:
    db.save(hero)

# Fetch all heroes
print("All Heroes:")
for h in db.all(Hero):
    ic(h)

# Fetch a hero by id
hero = db.get(Hero, id=2)
print("\nHero with ID=2:")
ic(hero)
