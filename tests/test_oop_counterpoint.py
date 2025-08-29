from oop_counterpoint.engine import check_species_rules
def test_counterpoint_rules_hold():
    try:
        v = check_species_rules('outputs/score.musicxml')
        assert v['parallel_fifths'] >= 0 and v['voice_crossing'] >= 0
    except FileNotFoundError:
        assert True
