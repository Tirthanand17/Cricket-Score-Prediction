import math

import pytest

from src.baseline import projected_total
from src.features import MatchState, build_features


def test_build_features_mid_innings():
    state = MatchState(
        current_runs=128,
        wickets_lost=3,
        balls_bowled=90,
        recent_runs=42,
        recent_balls=30,
    )

    features = build_features(state)

    assert features["overs_completed"] == 15.0
    assert features["balls_remaining"] == 30.0
    assert features["wickets_remaining"] == 7.0
    assert math.isclose(features["current_run_rate"], 128 / 15)
    assert math.isclose(features["recent_run_rate"], 42 / 5)


def test_zero_ball_state_is_safe():
    state = MatchState(current_runs=0, wickets_lost=0, balls_bowled=0)

    features = build_features(state)

    assert features["current_run_rate"] == 0.0
    assert features["recent_run_rate"] == 0.0
    assert projected_total(state) == 0.0


def test_invalid_wickets_are_rejected():
    state = MatchState(current_runs=100, wickets_lost=11, balls_bowled=60)

    with pytest.raises(ValueError, match="wickets_lost"):
        build_features(state)


def test_projection_is_above_current_score_when_scoring():
    state = MatchState(
        current_runs=120,
        wickets_lost=2,
        balls_bowled=84,
        recent_runs=50,
        recent_balls=30,
    )

    assert projected_total(state) > state.current_runs
