"""Main module for running."""
from typing import Union
from math import pi


class NotValidBall(Exception):
    """This is representation of not valid ball."""

    def __init__(self, radius: Union[float, int]) -> None:
        """Initialization method.

        Args:
            radius (Union[float, int]): radius not valid ball.
        """
        super().__init__(radius)
        self.radius = radius

    def __str__(self) -> None:
        """Exception in special format."""
        return 'Impossible to create ball with radius: {0}'.format(self.radius)


class Ball:
    """This is representation of ball."""

    DEGREES = 360

    def __init__(self, radius: Union[float, int]) -> None:
        """Initialization method.

        Args:
            radius (Union[float, int]): balls radius.

        Raises:
            NotValidBall : if the ball is impossible to create.
        """
        self.radius = radius
        if not self.checker():
            raise NotValidBall(self.radius)

    def motion(self, speed: Union[float, int], time: Union[float, int], acceleration: Union[float, int] = 0) -> float:
        """Count how many deegres did the ball turn. Round it to the 5th digit after point.

        Args:
            speed (Union[float, int]): the speed at which the ball is moving.
            time (Union[float, int]): the time the ball moves.
            acceleration (Union[float, int], optional): the acceleration at wich the ball is moving. Defaults to 0.

        Returns:
            float: how many deegres did the ball turn.
        """
        path = speed * time + (acceleration * time * time) / 2
        return round(path / ((2 * pi * self.radius) / Ball.DEGREES) % Ball.DEGREES, 5)

    def checker(self) -> bool:
        """Check ball.

        Returns:
            bool: True if ball is exists.
        """
        if self.radius != Union[int, float]:
            return False
        return self.radius > 0
