from __future__ import annotations

from .features import MatchState, build_features


def projected_total(state: MatchState) -> float:
    """Return a transparent baseline projection for comparison with ML models.

    The projection blends whole-innings and recent run rate, then applies a
    conservative wicket-resource factor. It is intentionally simple so an
    ML model can be evaluated against an explainable baseline.
    """

    features = build_features(state)

    current_rr = features["current_run_rate"]
    recent_rr = features["recent_run_rate"]
    balls_remaining = features["balls_remaining"]
    wickets_remaining = features["wickets_remaining"]

    blended_rr = (0.70 * current_rr) + (0.30 * recent_rr)

    # Preserve a transparent, bounded adjustment for batting resources.
    wicket_factor = 0.65 + (0.04 * wickets_remaining)
    wicket_factor = min(1.05, max(0.65, wicket_factor))

    remaining_overs = balls_remaining / 6.0
    projected_remaining = blended_rr * remaining_overs * wicket_factor

    return round(state.current_runs + projected_remaining, 2)
