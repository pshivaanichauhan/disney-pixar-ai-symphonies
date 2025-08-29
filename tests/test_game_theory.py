from game_theory.duelist import compute_stackelberg
def test_stackelberg_stable():
    res = compute_stackelberg()
    assert float(res.regret) < 0.05
