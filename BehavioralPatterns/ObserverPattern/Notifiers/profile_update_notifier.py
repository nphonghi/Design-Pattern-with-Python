from Base.observer import Observer
from game_result import GameResult

class ProfileUpdateNotifier(Observer):
    def __init__(self, subject):
        super().__init__(subject)
        self._subject.attach_observer(self)

    def notify(self, arg: object):
        if isinstance(self._subject, GameResult):
            print(f"Profile updated for player: {self._subject.get_player_name()} with result: {self._subject.get_result()}")
