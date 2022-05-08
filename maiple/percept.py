from reactivex import Subject
from melee.console import Console
from melee.enums import Menu


class VsMatch:
    __console: Console
    __game: Subject

    def __init__(self, console: Console):
        self.__game = Subject()
        self.__console = console

    def observe(self) -> Subject:
        return self.__game

    def play(self) -> None:
        while True:
            game_state = self.__console.step()
            if game_state.menu_state is not Menu.IN_GAME:
                self.__game.on_completed()
                return
            self.__game.on_next(game_state)

