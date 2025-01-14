# Module 1 - Mandatory Discussion - Classy Hints & Decorators

from dataclasses import dataclass, field
import uuid


@dataclass
class BoardGame(object):
    """One object of this class represents a boardgame's information:
    title, minimum number of players, maximum number of players,
    maximum expected time in minutes
    """

    title: str  # title of the game
    max_players: int = field(default=1)  # maximum number of players
    min_players: int = field(default=1)  # minimum number of players
    max_time: int = field(default=999)  # expected length of a game
    _ID: str = field(default_factory=uuid.uuid4)

    def __str__(self) -> str:
        # returns a nicely formatted string representation
        return "Title: {} Player count: {}-{} Time: {} minutes"\
            .format(self.title, self.min_players, self.max_players, \
                    self.max_time)
            
# getter functions

    def get_Maxtime(self) -> int:
        # prints the maximum time for a game
        # return str("Expected time: {}".format(self.max_time))
        return self.max_time

    def get_PlayerRange(self) -> str:
        # print the number of players
        return str("Number of players: {} - {}".format(self.min_players,
                                                       self.max_players))

    def get_ID(self) -> str:
        # return the ID of the game
        # added by CM Cheong
        return self._ID

# setter functions

    def add_Max_Players(self, count: int) -> None:
        # to add or change the number of max players
        if type(count) == int:
            self.max_players = count
            print("Maximum player count set.")
        else:
            print("Max players must be an integer.")

    def add_Min_PLayers(self, count: int) -> None:
        # to add or change the number of minimum players
        if type(count) == int:
            self.min_players = count
            print("Minimum player count set.")
        else:
            print("Minimum players must be an integer.")

    def add_Time(self, time: int) -> None:
        if type(time) == int:
            self.max_time = time
            print("Max time set.")
        else:
            print("You must provide the time in minutes")

