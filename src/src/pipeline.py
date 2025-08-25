import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

from music21 import stream, note, tempo, midi

DATA_PATH = "data/sample_script.txt"
OUT_DIR   = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)

def read_script(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
    return sentences

def emotion_series(sentences, window=3):
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()
    scores = [sia.polarity_scores(s)['compound'] for s in sentences]
    comp = pd.Series(scores)
    comp_s = comp.rolling(window, min_periods=1).mean()
    hope = comp_s.clip(lower=0.0)
    tension = (-comp_s).clip(lower=0.0)
    d = comp_s.diff().fillna(0.0)
    resolution = d.clip(lower=0.0)
    df = pd.DataFrame({"hope": hope.values, "tension": tension.values, "resolution": resolution.values})
    return df

def plot_emotion_heatmap(df):
    fig, ax = plt.subplots(figsize=(8, 3))
    im = ax.imshow(df.T, aspect="auto", cmap="magma")
    ax.set_yticks(range(3)); ax.set_yticklabels(["hope", "tension", "resolution"])
    ax.set_xticks([])
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    ax.set_title("Storybeats → Emotion Heatmap")
    out = os.path.join(OUT_DIR, "emotion_heatmap.png")
    plt.tight_layout(); plt.savefig(out, dpi=180); plt.close(fig)
    return out

def plot_motif_timeline(df):
    fig, ax = plt.subplots(figsize=(8, 2.5))
    ax.plot(df['hope'].values, label="hope")
    ax.plot(df['tension'].values, label="tension")
    ax.plot(df['resolution'].values, label="resolution")
    ax.set_title("Motif Drivers Over Time"); ax.set_xlabel("Beat (chunk)"); ax.legend()
    out = os.path.join(OUT_DIR, "motif_timeline.png")
    plt.tight_layout(); plt.savefig(out, dpi=180); plt.close(fig)
    return out

MOTIFS = {
    "hope":        [60, 64, 67, 72],
    "tension":     [60, 61, 63, 66],
    "resolution":  [67, 64, 60]
}

def generate_stream_from_emotions(df, bpm=96):
    s = stream.Stream(); s.append(tempo.MetronomeMark(number=bpm))
    eps = 1e-6
    arr = df[['hope','tension','resolution']].values
    arr = arr / (arr.sum(axis=1, keepdims=True) + eps)
    labels = ['hope','tension','resolution']
    for weights in arr:
        key = labels[int(np.argmax(weights))]
        for p in MOTIFS[key]:
            n = note.Note(p); n.quarterLength = 0.5
            s.append(n)
    return s

def write_midi(s, outpath):
    mf = midi.translate.streamToMidiFile(s)
    mf.open(outpath, 'wb'); mf.write(); mf.close()

if __name__ == "__main__":
    sentences = read_script(DATA_PATH)
    df = emotion_series(sentences, window=3)
    heat = plot_emotion_heatmap(df)
    tl   = plot_motif_timeline(df)
    print(f"Saved: {heat}\nSaved: {tl}")
    s = generate_stream_from_emotions(df, bpm=96)
    midi_path = os.path.join(OUT_DIR, "pixar_demo_motif.mid")
    write_midi(s, midi_path)
    print(f"Saved: {midi_path}")
