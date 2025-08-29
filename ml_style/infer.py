import argparse, mido, math

SCALE = [0,2,3,5,7,8,11]; BPM = 96

def motif(n):
    seq = [0,2,4,5,4,2,0]
    return [seq[i%len(seq)] for i in range(n)]

def build_midi(path, measures=16, ppq=480):
    mid = mido.MidiFile(ticks_per_beat=ppq)
    tr = mido.MidiTrack(); mid.tracks.append(tr)
    tr.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(BPM)))
    base = 60; m = motif(64); dur = ppq//2
    for i in range(measures*8):
        degree = m[i%len(m)]
        note = base + SCALE[degree % len(SCALE)]
        vel = 70 + int(25*math.sin(i/5))
        tr.append(mido.Message('note_on', note=note, velocity=vel, time=0 if i==0 else 0))
        tr.append(mido.Message('note_off', note=note, velocity=64, time=dur))
    mid.save(path)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    build_midi(args.out)
    print('Wrote', args.out)
