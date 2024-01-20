from itertools import product

dismissals_by_spinners = 70
balls_faced_against_spinners = 5449
strike_rate_against_spinners = 92.74
dismissals_by_pacers = 162
balls_faced_against_pacers = 9348
strike_rate_against_pacers = 94.06
number_of_spin_bowlers = 2
number_of_pace_bowlers = 4

probability_dismissal_per_ball_spinners = dismissals_by_spinners / balls_faced_against_spinners
balls_needed_for_century_against_spinners = 100 / (strike_rate_against_spinners / 100)
probability_not_getting_out_against_spinners = (1 - probability_dismissal_per_ball_spinners) ** balls_needed_for_century_against_spinners

probability_dismissal_per_ball_pacers = dismissals_by_pacers / balls_faced_against_pacers
balls_needed_for_century_against_pacers = 100 / (strike_rate_against_pacers / 100)
probability_not_getting_out_against_pacers = (1 - probability_dismissal_per_ball_pacers) ** balls_needed_for_century_against_pacers

probability_not_getting_out = ((number_of_spin_bowlers*probability_not_getting_out_against_spinners)+(number_of_pace_bowlers*probability_dismissal_per_ball_pacers))/(number_of_spin_bowlers+number_of_pace_bowlers)

balls_needed_for_century = ((number_of_spin_bowlers*balls_needed_for_century_against_spinners)+(number_of_pace_bowlers*balls_needed_for_century_against_pacers))/(number_of_spin_bowlers+number_of_pace_bowlers)

def scale_balls_left(balls):
    return (balls - balls_needed_for_century) / (299 - balls_needed_for_century) if balls > balls_needed_for_century else 0

scaled_balls_left = [scale_balls_left(balls) for balls in range(1, 300)]

conditions = {
    'boundary_distance': [1, 0],  # small (1), large (0)
    'hard_pitch': [1, 0],  # Yes (1), No (0)
    'cracks_in_pitch': [0, 1],  # Yes (0), No (1)
    'grass_on_pitch': [0, 1],  # Yes (0), No (1)
    'moisture_on_pitch': [0, 1],  # Yes (0), No (1)
    'temperature': [1, 0],  # high (1), low (0)
    'clear_skies': [1, 0],  # Yes (1), No (0)
    'balls_left': scaled_balls_left,  
    'other_guy_hitting_hard': [0, 1]  # Yes (0), No (1)
}

all_combinations = list(product(*conditions.values()))

scores_century = 0
does_not_score_century = 0

for combination in all_combinations:
    if sum(combination) >= 4.5:
        scores_century += 1
    else:
        does_not_score_century += 1

minimum_chance_of_scoring_century = probability_not_getting_out*(scores_century/len(all_combinations))

is_player_in_form = 1 #one or zero or somewhere in bw
opposition_difficulty = 1.3 #where 1 means Kohli has sr of his average
partner_stability = 1 #one or zero
momentum = 1.8 #where 2 means chasing a big score

multiplier = is_player_in_form + opposition_difficulty + partner_stability + momentum

chance_of_scoring_century = multiplier * minimum_chance_of_scoring_century
print(chance_of_scoring_century)