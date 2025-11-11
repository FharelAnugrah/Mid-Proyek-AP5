# View for leaderboard
def display_leaderboard(leaderboard_data):
    """
    Menampilkan tabel leaderboard top players
    
    Args:
        leaderboard_data (list): List of dict berisi data pemain
        
    Returns:
        None
    """
    print("\n" + "="*70)
    print("🏆 LEADERBOARD - TOP PLAYERS 🏆".center(70))
    print("="*70)
    
    if not leaderboard_data or not isinstance(leaderboard_data, list):
        print("Belum ada data pemain di leaderboard.")
        print("="*70)
        input("\nTekan Enter untuk kembali...")
        return
    
    # Header tabel
    print(f"{'Rank':<6} {'Username':<15} {'Class':<12} {'Floor':<7} {'Score':<10} {'Title':<15}")
    print("-"*70)
    
    # Data pemain
    for idx, player in enumerate(leaderboard_data, start=1):
        # Validasi setiap player
        if not isinstance(player, dict):
            continue
        
        # Ambil data dengan fallback value
        username = player.get('username', 'Unknown')[:15]  # Max 15 char
        class_name = player.get('class_name', 'N/A')[:12]  # Max 12 char
        floor = player.get('floor', 0)
        score = player.get('score', 0)
        title = player.get('title', 'N/A')[:15]  # Max 15 char
        
        # Medal untuk top 3
        if idx == 1:
            medal = "🥇"
        elif idx == 2:
            medal = "🥈"
        elif idx == 3:
            medal = "🥉"
        else:
            medal = f"{idx}."
        
        # Print data
        print(f"{medal:<6} {username:<15} {class_name:<12} "
              f"{floor:<7} {score:<10} {title:<15}")
    
    print("="*70)
    input("\nTekan Enter untuk kembali...")