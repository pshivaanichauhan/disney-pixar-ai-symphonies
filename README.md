# disney-pixar-storybeats
Story Beats to Music — Map narrative arcs into motif tokens that adaptively score emotion on screen.
📖 Overview
This project explores how narrative story beats from Disney–Pixar films can be translated into adaptive music motifs using AI.
By mapping arcs of emotion (hope, tension, triumph) into melodic tokens, the system demonstrates how machine learning can bridge storytelling and symphonic design.---

## 🚀 Workflow
1. **Story Beat Extraction**  
   - Parse screenplays and identify emotional arcs.  
   - Break down into labeled narrative tokens (hope, tension, resolution).  

2. **Motif Generation**  
   - Train ML models (Python + PyTorch) to map tokens → musical motifs.  
   - Encode motifs into MIDI/ABC notation.  

3. **Adaptive Playback**  
   - Real-time motif switching to reflect shifts in story beats.  
   - Supports orchestral layering and hybrid scoring.  ---

## 🛠 Tech Stack
- **Python 3.10**  
- **PyTorch / TensorFlow** for ML  
- **Music21** for motif encoding and analysis  
- **Jupyter Notebooks** for experiments  
- **MIDI/ABC Exporters** for DAW integration  
---

## 📂 Repo Structure

---

## 🔮 Future Work
- Expand training data with more Disney–Pixar scripts  
- Add emotion heatmaps alongside motifs  
- Experiment with orchestral layering for dynamic playback  
- Integrate with DAWs (Logic Pro, Ableton, Cubase) for demo scoring  

---

## ▶️ Usage

1. **Clone the repo**
   ```bash
   git clone https://github.com/pshivaanichauhan/disney-pixar-storybeats.git
   cd disney-pixar-storybeats
pip install -r requirements.txt
jupyter notebook notebooks/
