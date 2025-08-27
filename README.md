# 🎬 AI Symphonies for Disney & Pixar Storybeats  

This project translates **Disney Animation & Pixar storybeats** into **AI–generated symphonic themes and rhythm banks**, demonstrating graduate-level AI methods in symbolic music analysis.  
It reflects **Carnegie Hall’s Five Core Pillars**:

- 🎭 **Expressive Nuance (CV)** → emotion heatmaps from frames  
- 🤝 **Dynamic Collaboration (Game Theory)** → AI + human motif feedback  
- 🎨 **Stylistic Authenticity (ML)** → Pixar & Disney style + Beethoven depth  
- ⚙️ **Precision & Scalability (RPA)** → automated beat-to-motif pipeline  
- 📐 **Mathematical Depth (Algorithms & OOP)** → recursive counterpoint, syncopation, metric modulation  

---

## 📂 Project Structure
- `classifier_probs/` → probability outputs for motif classification  
- `data/` → input datasets / story scripts  
- `evolved_midis/` → generated motif `.mid` files  
- `heatmaps/` → emotional heatmaps from story frames  
- `motif_timelines/` → motif arc timelines (`.png`)  
- `notebooks/` → experiments & development notebooks  
- `outputs/` → organized final artifacts (heatmaps, timelines, MIDI)  
- `src/` → main pipeline scripts  

---

## 📊 Demo Artifacts

- **🎭 Emotion Heatmap**  
  `heatmaps/example_story.png`

- **📈 Motif Timeline (Story Arc)**  
  `motif_timelines/example_timeline.png`

- **🎼 Generated MIDI Motif**  
  `evolved_midis/story_motif.mid` ← download & play in any DAW  

---

## 🔎 What’s Inside (Highlights)
- Frame-level affect → **heatmap** of tension/hope/release  
- Beat segmentation → **timeline** of recurring motifs  
- Sequence modeling (LSTM/Transformer) → **MIDI motif** generation  
- Clean **RPA-style pipeline** so the whole thing runs end-to-end  
- Pixar + Disney **Rhythm Bank** → syncopation, metric modulations, counterpoint duets  

---

## ▶️ Run locally (Quick Start)

```bash
# 1) create & activate a venv (optional but recommended)
python3 -m venv .venv && source .venv/bin/activate

# 2) install dependencies
pip install -r requirements.txt

# 3) run the pipeline
python src/pipeline.py
```

---

## 🎶 Vision  
Merging Disney & Pixar narrative arcs with Beethoven-style motifs:  
An exploration of AI’s ability to generate emotionally adaptive soundtracks at symphonic scale.  

---

## 📜 License  
This project is released under the MIT License.
