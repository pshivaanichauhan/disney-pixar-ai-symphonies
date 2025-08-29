import argparse, os
from music21 import converter, instrument

def midi_to_musicxml(midi_path, xml_path):
    s = converter.parse(midi_path)
    p = instrument.Piano()
    for n in s.recurse().notes:
        n.storedInstrument = p
    s.write('musicxml', fp=xml_path)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='inp', required=True)
    ap.add_argument('--out', dest='out', required=True)
    args = ap.parse_args()
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    midi_to_musicxml(args.inp, args.out)
    print('Wrote', args.out)
