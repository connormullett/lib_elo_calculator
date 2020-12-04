
from lib_elo_calculator import calculate_adjusted_elo_rating

def test_elo_calculation():
    p_one_init, p_two_init = 2400, 2000
    player_one_win = True

    e_one, e_two = (2403, 1997)

    a_one, a_two = calculate_adjusted_elo_rating(
        p_one_init,
        p_two_init, 
        player_one_win
    )

    assert e_one == a_one
    assert e_two == a_two
