# Model for quest
class QuestData:
    def __init__(self, tipe, nama, reward_gold, reward_exp, kesulitan):
        self.tipe = tipe
        self.nama = nama
        self.reward_gold = reward_gold
        self.reward_exp = reward_exp
        self.kesulitan = kesulitan

    def tampilkan_info_quest(self):
        print(f"🎯 {self.nama} ({self.kesulitan})")
        print(f"Hadiah: {self.reward_gold} gold | {self.reward_exp} exp\n")
