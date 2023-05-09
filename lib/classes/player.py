class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username

    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
        
    
    def games_played(self, new_game=None):
        from classes.game import Game
        pass
    
    def played_game(self, game):
        pass
    
    def num_times_played(self, game):
        pass
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
