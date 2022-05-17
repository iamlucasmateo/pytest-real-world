import pytest

from logic.tennis import tennis_score

examples = (
    ("expected_score", "p1", "p2", "comment"), # parameter names
    [
        ("Love-All", 0, 0, "test name 1"), # parameter values
        ("Fifteen-All", 1, 1, "test name 2"),
        ("Thirty-All", 2, 2, "test comment 3")
    ]
)

# the comment parameter is not needed but helpful for error messages
@pytest.mark.parametrize(examples)
def test_game_scores(expected_score, p1, p2, comment): 
    assert expected_score == tennis_score(p1, p2)