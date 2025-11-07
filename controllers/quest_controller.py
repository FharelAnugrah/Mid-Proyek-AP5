# Controller for quest
import random
from models.quest_model import QuestData

class QuestController:
    def __init__(self, character):
        self.character = character
        self.active_quest = None

    def bikin_quest(self):
        tipe_quest = random.choice(["berburu", "pengumpulan"])
        kesulitan = random.choice(["mudah", "sedang", "sulit"])
        pengali = {"mudah": 1, "sedang": 1.5, "sulit": 2}[kesulitan]

        if tipe_quest == "berburu":
            musuh = random.choice(["goblin", "serigala", "bandit", "orc", "naga kecil"])
            gold_reward = int(random.randint(5, 15) * pengali)
            exp_reward = int(random.randint(10, 25) * pengali)
            quest = QuestData("berburu", f"Lawan {musuh}", gold_reward, exp_reward, kesulitan)

        else:
            material = random.choice(["kayu", "batu sihir", "herbal", "kulit binatang", "bijih besi"])
            gold_reward = int(random.randint(3, 10) * pengali)
            exp_reward = int(random.randint(8, 20) * pengali)
            quest = QuestData("pengumpulan", f"Kumpulkan {material}", gold_reward, exp_reward, kesulitan)

        self.active_quest = quest
        print("\nQuest Baru Diterima!")
        quest.tampilkan_info_quest()

    def selesaikan_quest(self):
        if not self.active_quest:
            print("❌ Tidak ada quest aktif!\n")
            return

        print(f"Menjalankan quest: {self.active_quest.nama}...")
        hasil = random.choices(["berhasil", "gagal"], weights=[0.8, 0.2])[0]

        if hasil == "berhasil":
            self.character.gold += self.active_quest.reward_gold
            self.character.exp += self.active_quest.reward_exp
            print(f"✅ Quest selesai! Kamu mendapat {self.active_quest.reward_gold} gold dan {self.active_quest.reward_exp} exp.")
            self.level_up()
        else:
            print("❌ Quest gagal! Tidak mendapat hadiah.")

        self.active_quest = None
        print(f"💰 Gold: {self.character.gold} | ⭐ EXP: {self.character.exp}\n")

    def level_up(self):
        target_exp = self.character.floor * 100
        if self.character.exp >= target_exp:
            self.character.exp -= target_exp
            self.character.floor += 1
            self.character.title = random.choice(["Petualang", "Pahlawan", "Ksatria", "Jawara"])
            print(f"🎉 Level UP! Sekarang Level {self.character.floor} - Title: {self.character.title}\n")
