from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MatchState:
    """Validated snapshot of a first-innings T20 match state."""

    current_runs: int
    wickets_lost: int
    balls_bowled: int
    recent_runs: int = 0
    recent_balls: int = 0
    max_balls: int = 120

    def validate(self) -> None:
        if self.current_runs < 0:
            raise ValueError("current_runs must be non-negative")
        if not 0 <= self.wickets_lost <= 10:
            raise ValueError("wickets_lost must be between 0 and 10")
        if not 0 <= self.balls_bowled <= self.max_balls:
            raise ValueError("balls_bowled must be between 0 and max_balls")
        if self.recent_runs < 0:
            raise ValueError("recent_runs must be non-negative")
        if not 0 <= self.recent_balls <= self.balls_bowled:
            raise ValueError("recent_balls must be between 0 and balls_bowled")
        if self.max_balls <= 0:
            raise ValueError("max_balls must be positive")


def build_features(state: MatchState) -> dict[str, float]:
    """Convert a live match state into simple model-ready numeric features."""

    state.validate()

    overs_completed = state.balls_bowled / 6.0
    current_run_rate = (
        state.current_runs / overs_completed if overs_completed > 0 else 0.0
    )
    recent_run_rate = (
        state.recent_runs / (state.recent_balls / 6.0)
        if state.recent_balls > 0
        else current_run_rate
    )

    balls_remaining = state.max_balls - state.balls_bowled
    wickets_remaining = 10 - state.wickets_lost

    return {
        "current_runs": float(state.current_runs),
        "wickets_lost": float(state.wickets_lost),
        "overs_completed": overs_completed,
        "current_run_rate": current_run_rate,
        "balls_remaining": float(balls_remaining),
        "wickets_remaining": float(wickets_remaining),
        "recent_run_rate": recent_run_rate,
    }
