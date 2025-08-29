# Disney/Pixar — Beethoven AI Mirror (Advanced)

This repository translates Disney & Pixar storybeats into AI-generated musical themes,
demonstrating advanced AI methods across Carnegie Hall’s five pillars applied in the
Disney–Pixar context.

## Carnegie Pillar → Disney/Pixar translation
- **CV** → shot/beat detection & dynamic curvature vs. story beats (emotion heatmaps from scenes)
- **Game Theory** → cooperative “emotion bank” vs. tension management (human-in-the-loop feedback)
- **ML Style** → leitmotif style engine (structured MIDI generation; Transformer-ready hooks)
- **RPA** → cue sheet → parts/stems delivery (MIDI→MusicXML auto-prep)
- **OOP/Algorithms** → “storybook cadence” rule-set for voice-leading, syncopation, meter shifts

## Quickstart
```bash
pip install -r requirements.txt
pytest                     # run tests
make all                   # build MIDI → MusicXML → WAV → CV plots
```

## Artifacts built by CI
- `outputs/score.musicxml`
- `outputs/audio_preview.wav`
- `outputs/figures/dynamic_curve.png`
- `outputs/figures/motif_histogram.png`
