import unittest

from logic.tennis import tennis_score

test_case_data = {
    "even_scores": [
        ("Love-All", 0, 0),
        ("Fifteen-All", 1, 1),
        ("Thirty-All", 1, 1),
    ],
    "early_games_with_uneven_scores": [
        ("Fifteen-Love", 1, 0),
        ("Thirty-Love", 2, 0),
        ("Forty-Love", 3, 0),
         ("Love-Thirty", 0, 2)
    ]
}

def tennis_test_template(*args):
    def internal(self):
        self.assert_tennis_score(*args)
    return internal

class TennisTest(unittest.TestCase):
    
    # custom assert for parameterization
    def assert_tennis_score(self, expected, points1, points2):
        self.assertEqual(expected, tennis_score(points1, points2))
 
    def test_even_scores_zero_points(self):
        self.assertEqual("Love-All", tennis_score(0, 0))
     
    def test_even_scores_one_point(self):
        self.assert_tennis_score("Fifteen-All", 1, 1)
    
    def test_even_scores_two_points(self):
        self.assert_tennis_score("Thirty-All", 2, 2)
    
    def test_uneven_early_game(self):
        self.assert_tennis_score("Fifteen-Love", 1, 0)
        self.assert_tennis_score("Thirty-Love", 2, 0)
        self.assert_tennis_score("Forty-Love", 3, 0)
        self.assert_tennis_score("Love-Thirty", 0, 2)

# "metaprogramming" parameterization
# creating tests for each case by setting attributes name and test
for behaviour, test_cases in test_case_data.items():
    for tennis_test_case_data in test_cases:
        expected, p1, p2 = tennis_test_case_data
        test_name = "test_{behaviour}_{p1}_{p2}"
        test_case = tennis_test_template(*tennis_test_case_data) # this is a function
        setattr(TennisTest, test_name, test_case)