import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from music21 import note, stream, tempo, midi

# Data paths
DATA_PATH = "data/sample_script.txt"
OUT_DIR = "out/"
os.makedirs(OUT_DIR, exist_ok=True)

# ---- Script Reader ----
def read_script(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
    return sentences

# ---- Emotion Extractor ----
def compute_emotions(sentences, window=3):
    import nltk
    nltk.download("vader_lexicon", quiet=True)
    sia = SentimentIntensityAnalyzer()
    scores = [sia.polarity_scores(s)["compound"] for s in sentences]
    series = pd.Series(scores)

    comp = series.rolling(window, min_periods=1).mean()
    hope = np.clip(comp, 0, 1.0)
    tension = np.clip(-comp, 0, 1.0)
    resolution = hope.cumsum() / (np.arange(len(hope)) + 1)

    return pd.DataFrame({
        "hope": hope.values,
        "tension": tension.values,
        "resolution": resolution.values
    })

# ---- Visuals ----
def plot_emotion_heatmap(df):
    fig, ax = plt.subplots(figsize=(8, 3))
    cax = ax.matshow(df.T, aspect="auto", cmap="magma")
    ax.set_yticks(range(3))
    ax.set_yticklabels(["hope", "tension", "resolution"])
    fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)
    plt.title("Story Arcs → Emotion Heatmap")
    plt.savefig(os.path.join(OUT_DIR, "emotion_heatmap.png"), dpi=180)
    plt.close(fig)

def plot_motif_timeline(df):
    fig, ax = plt.subplots(figsize=(8, 2.5))
    for col in df.columns:
        ax.plot(df[col].values, label=col)
    ax.set_xlabel("Beat")
    ax.set_ylabel("Intensity")
    ax.legend()
    plt.title("Motif Timeline")
    plt.savefig(os.path.join(OUT_DIR, "motif_timeline.png"), dpi=180)
    plt.close(fig)

# ---- Motifs ----
MOTIFS = {
    "hope": [60, 64, 67, 72],
    "tension": [62, 65, 69],
    "resolution": [67, 64, 60]
}

def generate_stream_from_emotions(df, bpm=96):
    s = stream.Stream()
    s.append(tempo.MetronomeMark(number=bpm))

    for idx in range(len(df)):
        values = df.iloc[idx]
        dominant = values.idxmax()  # pick the strongest emotion
        motif = MOTIFS[dominant]
        for pitch in motif:
            n = note.Note(pitch)
            n.quarterLength = 0.5
            s.append(n)
    return s

def write_midi(s, filename="story_motif.mid"):
    mf = midi.translate.streamToMidiFile(s)
    mf.open(os.path.join(OUT_DIR, filename), 'wb')
    mf.write()
    mf.close()

# ---- Main Run ----
if __name__ == "__main__":
    sentences = read_script(DATA_PATH)
    df = compute_emotions(sentences)

    plot_emotion_heatmap(df)
    plot_motif_timeline(df)

    stream_out = generate_stream_from_emotions(df)
    write_midi(stream_out)
    print("✅ Outputs saved in", OUT_DIR)
