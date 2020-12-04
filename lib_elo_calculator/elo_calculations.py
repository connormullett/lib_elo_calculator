
import numpy as np


def calculate_adjusted_elo_rating(player_one_rating: int, player_two_rating: int, player_one_win: bool, k_factor=32) -> (int, int):
  """
  Calculates new elo scores for two players

  :param player_one_rating: first player's original rating
  :param player_two_rating: second player's origin rating
  :param player_one_win: boolean value describing if player one was the victor
  :param k_factor: the `k` factor used. Defaults to the chess value of 32
  :return: updated elo scores for both players as a tuple (player_one, player_two)
  """

  ratings = [player_one_rating, player_two_rating]
  t_one, t_two = _transform_ratings(ratings)

  e_one, e_two = calculate_expected_score(t_one, t_two)

  s_one, s_two = (1, 0) if player_one_win else (0, 1)

  u_one = player_one_rating + k_factor * (s_one - e_one)
  u_two = player_two_rating + k_factor * (s_two - e_two)

  out = np.round((u_one, u_two))

  return out


def calculate_expected_score(rating_one: int, rating_two: int) -> (float, float):
  """
  finds individual probability between two ratings
  :param rating_one: player_one's initial rating
  :param rating_two: player_two's initial rating
  :return: tuple containing player one and player two's expected outcome respectively 
  """
  rated_sum = rating_one + rating_two

  expected_one = rating_one / rated_sum
  expected_two = rating_two / rated_sum

  return expected_one, expected_two


def _transform_rating(rating: int) -> int:
  """
  helper function that transforms initial rating
  :param rating: the initial rating
  :return: new transformed rating as a power of 10
  """
  return int(np.power(10, (rating / 400)))


def _transform_ratings(ratings: (int, int)) -> (int, int):
  """
  _transform_rating wrapper to accept multiple values
  :param ratings: tuple of 2 values containing initial ratings for both players
  :return: transformed ratings for (player_one, player_two) as a tuple
  """
  out_ratings = []

  for rating in ratings:
    out_ratings.append(_transform_rating(rating))

  return tuple(out_ratings)
