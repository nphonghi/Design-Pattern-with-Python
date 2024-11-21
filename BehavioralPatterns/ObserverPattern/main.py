from game_result import GameResult
from Notifiers.profile_update_notifier import ProfileUpdateNotifier
from Notifiers.result_notifier import ResultNotifier

if __name__ == "__main__":
    game_result = GameResult()

    ResultNotifier(game_result)
    ProfileUpdateNotifier(game_result)
    
    game_result.set_result("Win", "Player1")
    print("-------------------------------")
