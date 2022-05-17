score_names = ["Love", "Fifteen", "Thirty", "Forty"]

def tennis_score(points1, points2):
    points1 = score_names[points1]
    points2 = score_names[points2]
    if points2 == points1:
        return f"{points1}-All"
    return f"{points1}-{points2}"