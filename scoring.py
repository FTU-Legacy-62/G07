"""
scoring.py - Final game results, bias definitions, and how-to-avoid guidance.
"""

from dataclasses import dataclass
from typing import Dict, List

from config import COLOR_DANGER, COLOR_SUCCESS, COLOR_WARNING, STARTING_CAPITAL


RATIONALITY_BANDS = [
    (0, 65, "Poor", COLOR_DANGER),
    (65, 80, "Average", COLOR_WARNING),
    (80, 101, "Good", COLOR_SUCCESS),
]


@dataclass
class GameResult:
    player_name: str
    initial_capital: float
    final_value: float
    total_return_pct: float
    bias_results: Dict[str, Dict]
    total_bias_score: int
    rationality_score: float


def compute_results(
    player_name: str,
    log: List[Dict],
    bias_results: Dict[str, Dict],
) -> GameResult:
    """Compute final performance and rationality score."""

    final_value = (
        log[-1].get("portfolio_value_end", log[-1].get("portfolio_value"))
        if log else float(STARTING_CAPITAL)
    )
    total_return_pct = (final_value - STARTING_CAPITAL) / STARTING_CAPITAL * 100
    total_bias_score = sum(b["score"] for b in bias_results.values())

    trade_rounds = sum(1 for row in log if row.get("action") in {"buy", "sell"})
    invested_rounds = sum(
        1
        for row in log
        if float(row.get("shares_before") or 0.0) > 0
        or float(row.get("shares_after") or 0.0) > 0
    )
    round_count = len(log) or 1
    trade_ratio = min(1.0, trade_rounds / 3)
    exposure_ratio = invested_rounds / round_count
    engagement_ratio = min(1.0, 0.45 * trade_ratio + 0.55 * exposure_ratio)
    participation_score = (
        0
        if trade_rounds == 0 and invested_rounds == 0
        else 6 + 9 * engagement_ratio
    )

    return_component = max(-25, min(25, total_return_pct))
    return_score = 30 + (return_component / 25) * 15
    bias_component = min(total_bias_score, 40)
    bias_score = (1 - bias_component / 40) * 40
    raw_rationality_score = return_score + bias_score + participation_score
    if total_return_pct < 0 and total_bias_score >= 10:
        compound_penalty = min(
            15,
            abs(total_return_pct) * 0.8 + max(0, total_bias_score - 8) * 1.2,
        )
        raw_rationality_score -= compound_penalty
    if trade_rounds == 0 and invested_rounds == 0:
        raw_rationality_score = min(raw_rationality_score, 55)
    rationality_score = round(max(0, min(100, raw_rationality_score)), 1)

    return GameResult(
        player_name=player_name,
        initial_capital=float(STARTING_CAPITAL),
        final_value=final_value,
        total_return_pct=total_return_pct,
        bias_results=bias_results,
        total_bias_score=total_bias_score,
        rationality_score=rationality_score,
    )


def get_rationality_band(score: float) -> tuple[str, str]:
    """Return the display label and color for a rationality score."""

    for lower, upper, label, color in RATIONALITY_BANDS:
        if lower <= score < upper:
            return label, color
    return RATIONALITY_BANDS[-1][2], RATIONALITY_BANDS[-1][3]


BIAS_DEFINITIONS = {
    "Overconfidence": (
        "Market participants overestimate their own intuitive ability or reasoning. "
        "It may appear as illusion of knowledge, prediction overconfidence, certainty "
        "overconfidence, or self-attribution."
    ),
    "Herding": (
        "Herding behavior is a form of regret aversion where participants go with "
        "consensus or popular opinion, partly because being wrong with others feels "
        "less blameworthy."
    ),
    "Availability": (
        "Individuals put undue emphasis on information that is readily available, "
        "recent, vivid, easy to recall, or based narrowly on personal experience."
    ),
    "Framing": (
        "Decisions are affected by how a question, data, or outcome is framed, "
        "rather than only by the underlying economic facts."
    ),
    "Loss Aversion": (
        "Individuals feel more pain from a loss than pleasure from an equal gain. "
        "They may take risk to avoid realizing losses or hold deteriorated assets "
        "in hope of recovery."
    ),
    "Disposition Effect": (
        "Investors have a disposition to sell winning investments too early and "
        "ride or hold losing investments too long."
    ),
}


BIAS_AVOIDANCE = {
    "Overconfidence": (
        "Use a pre-defined trading plan, limit position size, and check whether "
        "the decision is supported by fundamentals rather than personal confidence. "
        "Review past wrong decisions to avoid overestimating forecasting ability."
    ),
    "Herding": (
        "Do not follow the crowd automatically. Compare the crowd signal with "
        "fundamentals, valuation, and risk level before trading. A decision should "
        "be made only when independent financial evidence also supports the action."
    ),
    "Availability": (
        "Avoid reacting only to the most recent or most visible news. Check whether "
        "the news has a real impact on revenue, cost, margin, or risk. Compare "
        "short-term headlines with longer-term fundamentals before making a decision."
    ),
    "Framing": (
        "Separate the wording of the news from the underlying financial facts. "
        "Check whether positive or negative framing is supported by actual "
        "fundamentals, valuation, and expected earnings impact."
    ),
    "Loss Aversion": (
        "Set clear stop-loss or review rules before entering a position. Do not "
        "hold a losing position only to avoid realizing the loss. Reassess whether "
        "the original investment reason is still valid after bad news or price declines."
    ),
    "Disposition Effect": (
        "Do not sell winners too early just to lock in small gains, and do not hold "
        "losers too long hoping they will recover. Evaluate each position based on "
        "future fundamentals, not only current profit or loss."
    ),
}


def get_suggestion(bias_name: str, tier: str) -> str:
    """Return how-to-avoid guidance. Tier is kept for backward compatibility."""

    return BIAS_AVOIDANCE.get(bias_name, "")


def get_bias_definition(bias_name: str) -> str:
    """Return CFA/textbook-aligned definition used in the final breakdown."""

    return BIAS_DEFINITIONS.get(bias_name, "")
