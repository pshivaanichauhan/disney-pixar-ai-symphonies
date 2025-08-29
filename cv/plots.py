import argparse, os
from music21 import converter, note
import matplotlib.pyplot as plt

def extract_dynamics(stream):
    dyn = []; t = 0.0
    for el in stream.flatten().notesAndRests:
        dur = float(el.quarterLength)
        vel = 64
        if hasattr(el, 'volume') and el.volume and el.volume.velocity is not None:
            vel = int(el.volume.velocity)
        dyn.append((t, vel)); t += dur
    return dyn

def motif_histogram(stream):
    counts = {}
    for n in stream.recurse().getElementsByClass(note.Note):
        p = n.pitch.nameWithOctave
        counts[p] = counts.get(p, 0) + 1
    return counts

def main(xml_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    s = converter.parse(xml_path)
    curve = extract_dynamics(s)
    if curve:
        xs, ys = zip(*curve)
        plt.figure(); plt.plot(xs, ys)
        plt.xlabel('Beats'); plt.ylabel('Velocity'); plt.title('Dynamic Curve')
        plt.savefig(os.path.join(out_dir, 'dynamic_curve.png'), dpi=160); plt.close()
    hist = motif_histogram(s)
    if hist:
        items = sorted(hist.items(), key=lambda x: -x[1])[:20]
        labels, vals = zip(*items)
        plt.figure(); plt.bar(labels, vals); plt.xticks(rotation=45, ha='right')
        plt.title('Motif/Note Histogram (top20)'); plt.tight_layout()
        plt.savefig(os.path.join(out_dir, 'motif_histogram.png'), dpi=160); plt.close()

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='inp', required=True)
    ap.add_argument('--out', dest='out', required=True)
    args = ap.parse_args()
    main(args.inp, args.out)
