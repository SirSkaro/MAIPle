from reactivex import Subject
from melee import Console


class Game:
    _console: Console
    _subject: Subject

    def __init__(self, console: Console):
        self._subject = Subject()
        self._console = console
        self._should_quit = False

    def observe(self) -> Subject:
        return self._subject

    def start(self) -> None:
        while True:
            if self._should_quit:
                self._subject.on_completed()
                break

            game_state = self._console.step()
            if game_state is None:
                continue
            self._subject.on_next(game_state)
