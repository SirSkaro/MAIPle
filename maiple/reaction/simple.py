from typing import List

from melee import GameState, PlayerState, Button
from melee import Action as Animation

from maiple.actuator import Actuator, Action


class JumpActuator(Actuator):
    _player_port: int

    def __init__(self, player_port):
        self._player_port = player_port

    def to_action(self, state: GameState) -> List[Action]:
        player_state = state.players[self._player_port]
        if state.distance > 50 and self._can_jump(player_state):
            return [lambda controller: controller.press_button(Button.BUTTON_X)]
        elif self._is_airborn(player_state) and self._is_holding(player_state, Button.BUTTON_X):
            return [lambda controller: controller.release_button(Button.BUTTON_X)]
        return self._no_ops(1)

    def _can_jump(self, player_state: PlayerState) -> bool:
        current_animation = player_state.action
        return current_animation is Animation.STANDING

    def _is_airborn(self, player_state: PlayerState) -> bool:
        current_animation = player_state.action
        return current_animation in [Animation.JUMPING_FORWARD, Animation.JUMPING_BACKWARD,
                                     Animation.JUMPING_ARIAL_FORWARD, Animation.JUMPING_ARIAL_BACKWARD]

    def _is_holding(self, player_state: PlayerState, button) -> bool:
        controller_state = player_state.controller_state
        return controller_state.button[button]
