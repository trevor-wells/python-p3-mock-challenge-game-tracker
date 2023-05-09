class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and self._title == None:
            self._title = new_title

    def results(self, new_result=None):
        from classes.result import Result
        pass
    
    def players(self, new_player=None):
        from classes.player import Player
        pass
    
    def average_score(self, player):
        pass