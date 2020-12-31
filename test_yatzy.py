from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance_scores_sum_of_all_dice():
        assert 16 == Yatzy([3, 3, 4, 5, 1]).score('chance')
        assert 15 == Yatzy([2, 3, 4, 5, 1]).score('chance')
        assert 20 == Yatzy([4, 4, 4, 4, 4]).score('chance')


def test_yatzy_scores_50():
        assert 50 == Yatzy([4, 4, 4, 4, 4]).score('yatzy')
        assert 50 == Yatzy([6, 6, 6, 6, 6]).score('yatzy')
        assert 50 == Yatzy([2, 2, 2, 2, 2]).score('yatzy')
        assert 0 == Yatzy([6, 6, 6, 6, 3]).score('yatzy')


def test_1s():
        assert 1 == Yatzy([1, 2, 3, 4, 5]).score('ones')
        assert 2 == Yatzy([1, 2, 1, 4, 5]).score('ones')
        assert 0 == Yatzy([6, 2, 2, 4, 5]).score('ones')
        assert 4 == Yatzy([1, 2, 1, 1, 1]).score('ones')

def test_2s():
        assert 4 == Yatzy([1, 2, 3, 2, 6]).score('twos')
        assert 4 == Yatzy([6, 2, 2, 4, 5]).score('twos')
        assert 10 == Yatzy([2, 2, 2, 2, 2]).score('twos')
        assert 8 == Yatzy([2, 2, 2, 4, 2]).score('twos')
  

def test_3s():
        assert 3 == Yatzy([1, 2, 3, 2, 6]).score('threes')
        assert 0 == Yatzy([1, 2, 5, 2, 6]).score('threes')
        assert 6 == Yatzy([1, 2, 3, 2, 3]).score('threes')
        assert 12 == Yatzy([2, 3, 3, 3, 3]).score('threes')
  

def test_4s():
        assert 12 == Yatzy([4, 4, 4, 5, 5]).score('fours')
        assert 8 == Yatzy([4, 4, 5, 5, 5]).score('fours')
        assert 4 == Yatzy([4, 5, 5, 5, 5]).score('fours')
        assert 0 == Yatzy([5, 5, 5, 5, 5]).score('fours')
  

def test_5s():
        assert 5 == Yatzy([4, 4, 4, 4, 5]).score('fives')
        assert 10 == Yatzy([4, 4, 4, 5, 5]).score('fives')
        assert 15 == Yatzy([4, 4, 5, 5, 5]).score('fives')
        assert 20 == Yatzy([4, 5, 5, 5, 5]).score('fives')
  

def test_6s():
        assert 0 == Yatzy([4, 4, 4, 5, 5]).score('sixes')
        assert 6 == Yatzy([4, 4, 6, 5, 5]).score('sixes')
        assert 12 == Yatzy([4, 4, 6, 5, 6]).score('sixes')
        assert 18 == Yatzy([6, 5, 6, 6, 5]).score('sixes')
  

def test_pair():
        assert 6 == Yatzy([3, 4, 3, 5, 6]).score('pair')
        assert 12 == Yatzy([3, 4, 6, 5, 6]).score('pair')
        assert 10 == Yatzy([5, 3, 3, 3, 5]).score('pair')
        assert 12 == Yatzy([5, 3, 6, 6, 5]).score('pair')
  

def test_two_pairs():
        assert 16 == Yatzy([3, 3, 5, 4, 5]).score('two_pairs')
        assert 18 == Yatzy([3, 3, 6, 6, 6]).score('two_pairs')
        assert 0 == Yatzy([3, 3, 6, 5, 4]).score('two_pairs')
        assert 14 == Yatzy([3, 3, 6, 4, 4]).score('two_pairs')


def test_three_of_a_kind():
        assert 9 == Yatzy([3, 3, 3, 4, 5]).score('three_of_a_kind')
        assert 15 == Yatzy([5, 3, 5, 4, 5]).score('three_of_a_kind')
        assert 9 == Yatzy([3, 3, 3, 3, 5]).score('three_of_a_kind')
        assert 6 == Yatzy([2, 3, 2, 2, 5]).score('three_of_a_kind')
  

def test_four_of_a_kind():
        assert 12 == Yatzy([3, 3, 3, 3, 5]).score('four_of_a_kind')
        assert 20 == Yatzy([5, 5, 5, 4, 5]).score('four_of_a_kind')
        assert 12 == Yatzy([3, 3, 3, 3, 3]).score('four_of_a_kind')
        assert 0  == Yatzy([3, 3, 3, 2, 1]).score('four_of_a_kind')
  

def test_small_straight():
        assert 30 == Yatzy([1, 2, 3, 4, 5]).score('small_straight')
        assert 30 == Yatzy([2, 3, 4, 5, 1]).score('small_straight')
        assert 0 == Yatzy([1, 2, 2, 4, 5]).score('small_straight')
        assert 30 == Yatzy([1, 2, 3, 4, 3]).score('small_straight')
  

def test_large_straight():
        assert 40 == Yatzy([6, 2, 3, 4, 5]).score('large_straight')
        assert 40 == Yatzy([2, 3, 4, 5, 6]).score('large_straight')
        assert 0 == Yatzy([1, 2, 2, 4, 5]).score('large_straight')


def test_full_house():
        assert 25 == Yatzy([6, 2, 2, 2, 6]).score('full_house')
        assert 0 == Yatzy([2, 3, 4, 5, 6]).score('full_house')
   