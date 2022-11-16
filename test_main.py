"""Module for testing."""
from main import Ball, NotValidBall
import pytest


test_for_not_valid_ball = [(-1, False), (0, False), ('sss', False), ([1, 2, 3], False), ((1, 2), False), ({1: 2}, False), ({1}, False)]


@pytest.mark.xfail(raises=NotValidBall)
@pytest.mark.parametrize('radius, expectation', test_for_not_valid_ball)
def test_not_val(radius, expectation):
    """Test for not valid ball."""
    assert Ball(radius).checker() == expectation


test_for_val_ball = [(1, True), (5.0, True), (10.1, True), (10000, True)]


@pytest.mark.parametrize('radius, expectation', test_for_val_ball)
def test_val(radius, expectation):
    """Test for valid ball."""
    assert Ball(radius).checker() == expectation


test_for_radius = [(1), (5), (7.0), (10000.1)]


@pytest.mark.parametrize('radius', test_for_radius)
def test_radius(radius):
    """Test for radius."""
    assert Ball(radius).radius == radius


test_for_uniform_motion = [(5, 5, 5, 286.4789), (6, 1, 1000, 189.29659), (1000, 0.1, 1000, 5.72958)]


@pytest.mark.parametrize('radius, speed, time, expectation', test_for_uniform_motion)
def test_uniform(radius, speed, time, expectation):
    """Test for uniform motion."""
    assert Ball(radius).motion(speed, time) == expectation


test_for_uniformly_accelerated_motion = [(5, 10, 10, 10, 35.49354), (2, 0, 1, -10, 216.76055), (1, 1, 1, 1, 85.94367)]


@pytest.mark.parametrize('radius, speed, time, acceleration, expectation', test_for_uniformly_accelerated_motion)
def test_uniformly_accelerated(radius, speed, time, acceleration, expectation):
    """Test for uniformly accelerated motion."""
    assert Ball(radius).motion(speed, time, acceleration) == expectation
