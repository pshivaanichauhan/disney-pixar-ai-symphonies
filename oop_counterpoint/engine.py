from music21 import converter, interval, chord

def check_species_rules(xml_path):
    s = converter.parse(xml_path).chordify()
    violations = {'parallel_fifths':0, 'voice_crossing':0}
    last_inter = None; last_pitches = None
    for c in s.recurse().getElementsByClass(chord.Chord):
        if len(c.pitches) < 2: 
            continue
        pitches = sorted([p.midi for p in c.pitches])
        if last_pitches and (pitches[0] > last_pitches[1] or pitches[1] < last_pitches[0]):
            violations['voice_crossing'] += 1
        inter = interval.Interval(pitches[0], pitches[1]).semitones % 12
        if last_inter == 7 and inter == 7:
            violations['parallel_fifths'] += 1
        last_inter, last_pitches = inter, pitches
    return violations
