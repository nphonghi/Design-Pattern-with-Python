from Base.observer import Observer
from game_result import GameResult

class ResultNotifier(Observer):
    def __init__(self, subject):
        super().__init__(subject)
        self._subject.attach_observer(self)

    def notify(self, arg: object):
        if isinstance(self._subject, GameResult):
            print(f"Player {self._subject.get_player_name()} has been notified: Your game result '{self._subject.get_result()}' has been saved.")
