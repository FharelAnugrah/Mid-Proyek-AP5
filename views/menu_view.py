# View for menu
from controllers.character_controller import create_character, load_character_by_user_id
from controllers.leaderboard_controller import get_leaderboard
from controllers.quest_controller import QuestController
from views.leaderboard_view import display_leaderboard
from controllers.shop_controller import open_shop
from controllers.character_controller import inventory_menu;

def main_menu(user):
    while True:
        print("\n1. Create a character")
        print("2. Quest")
        print("3. Leaderboard")
        print("4. Shop")
        print("5. inventory")
        print("6. Delete account")
        pilihan = input("Pilih menu: ")
        
        try:
            if pilihan == "1":
                create_character(user["id"])
            elif pilihan == "2":
                character = load_character_by_user_id(user["id"])
                quest_controller = QuestController(character)
                quest_controller.bikin_quest()
            elif pilihan == "3":
                leaderboard_data = get_leaderboard()
                display_leaderboard(leaderboard_data)
            elif pilihan == "4":
                character = load_character_by_user_id(user["id"])
                open_shop(character)
            elif pilihan == "5":
                character = load_character_by_user_id(user["id"])
                inventory_menu(character.character_id)
            else:
                print("belum dibuat")
        except Exception as e:
            print("Terjadi error:", e)