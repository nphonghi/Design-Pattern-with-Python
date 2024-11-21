from Base.subject import Subject

class GameResult(Subject):
    def __init__(self):
        super().__init__()
        self.__result = None
        self.__player_name = None

    def get_result(self):
        return self.__result
    
    def get_player_name(self):
        return self.__player_name
    
    def set_result(self, result, player_name):
        self.__result = result
        self.__player_name = player_name
        # Receive result, calculate win rate and update to player profile
        self.__profile_updated()

    def __profile_updated(self):
        self.notify_observers(None)
