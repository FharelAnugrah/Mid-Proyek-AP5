# controller_character.py
from models.character_model import Character
from utils.database import db, cursor

class Archmage(Character):
    def __init__(self, user_id: int):
        super().__init__(user_id, "Archmage", hp=200, energy=250, defense=100, damage=75)
    def special_attack(self, target):
        if self.energy >= 30:
            dmg = int(self.damage * 1.5)
            target.hp -= dmg
            self.energy -= 30
            print(f"{self.class_name} melempar bola api ({dmg} dmg)")
        else:
            print("Energi tidak cukup!")

class Guardian(Character):
    def __init__(self, user_id: int):
        super().__init__(user_id, "Guardian", hp=350, energy=100, defense=200, damage=40)

class Marksman(Character):
    def __init__(self, user_id: int):
        super().__init__(user_id, "Marksman", hp=220, energy=120, defense=120, damage=90)

class Assassin(Character):
    def __init__(self, user_id: int):
        super().__init__(user_id, "Assassin", hp=180, energy=150, defense=80, damage=100)

class Fighter(Character):
    def __init__(self, user_id: int):
        super().__init__(user_id, "Fighter", hp=250, energy=130, defense=150, damage=80)


def create_character(user_id: int):
    print("\n=== PEMBUATAN KARAKTER BARU ===")
    print("1. Archmage  - Penyihir kuat dengan energi besar")
    print("2. Guardian  - Pelindung tangguh dengan pertahanan tinggi")
    print("3. Marksman  - Pemanah cepat dengan serangan tajam")
    print("4. Assassin  - Pembunuh lincah dengan serangan mematikan")
    print("5. Fighter   - Petarung seimbang dengan daya tahan baik")

    choice = input("Masukkan pilihan (1-5): ").strip()

    class_map = {
        "1": Archmage,
        "2": Guardian,
        "3": Marksman,
        "4": Assassin,
        "5": Fighter
    }

    if choice not in class_map:
        print("Pilihan tidak valid! Silakan coba lagi.\n")
        return create_character(user_id)

    char = class_map[choice](user_id)

    try:
        # Pastikan user belum punya karakter sebelumnya
        cursor.execute("SELECT id FROM characters WHERE user_id = %s", (user_id,))
        existing_char = cursor.fetchone()
        if existing_char:
            print("\n❌ User ini sudah memiliki karakter! Tidak bisa membuat lagi.")
            return None

        # Simpan karakter baru
        cursor.execute("""
            INSERT INTO characters 
            (user_id, class_name, hp, energy, defense, damage, gold, exp, floor, title, score)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            char.user_id,
            char.class_name,
            char.hp,
            char.energy,
            char.defense,
            char.damage,
            char.gold,
            char.exp,
            char.floor,
            char.title,
            char.score
        ))
        db.commit()

        # Ambil ID karakter yang baru dibuat
        cursor.execute("SELECT LAST_INSERT_ID()")
        char_id = cursor.fetchone()[0]

        # Tambahkan item awal ke inventory
        starter_items = [("Small Potion", 3), ("Wooden Sword", 1)]
        cursor.executemany("""
            INSERT INTO inventory_items (character_id, item_name, quantity)
            VALUES (%s, %s, %s)
        """, [(char_id, name, qty) for name, qty in starter_items])
        db.commit()

        print(f"\n✅ Karakter '{char.class_name}' berhasil dibuat untuk User ID {user_id}!")
        print("🎒 Item awal: Small Potion x3, Wooden Sword x1")
        char.show_status()

    except Exception as e:
        db.rollback()
        print("⚠️ Terjadi kesalahan saat menyimpan karakter:", e)

    return char
