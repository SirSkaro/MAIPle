from reactivex import Subject
from melee import Console
from melee import Menu


class VsMatch:
    _console: Console
    _game: Subject

    def __init__(self, console: Console):
        self._game = Subject()
        self._console = console

    def observe(self) -> Subject:
        return self._game

    def play(self) -> None:
        while True:
            game_state = self._console.step()
            if game_state is None:
                continue
            elif game_state.menu_state is Menu.IN_GAME:
                self._game.on_next(game_state)
            else:
                self._game.on_completed()
                return

