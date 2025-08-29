import os, glob, subprocess, sys

def test_artifacts_exist_after_build():
    subprocess.run([sys.executable,'ml_style/infer.py','--out','outputs/score.mid'], check=True)
    subprocess.run([sys.executable,'rpa_orchestration/build_parts.py','--in','outputs/score.mid','--out','outputs/score.musicxml'], check=True)
    subprocess.run([sys.executable,'oop_counterpoint/render_audio.py','--in','outputs/score.mid','--out','outputs/audio_preview.wav'], check=True)
    subprocess.run([sys.executable,'cv/plots.py','--in','outputs/score.musicxml','--out','outputs/figures'], check=True)
    assert os.path.exists('outputs/score.musicxml')
    assert os.path.getsize('outputs/score.musicxml') > 500
    assert os.path.exists('outputs/audio_preview.wav')
    assert os.path.getsize('outputs/audio_preview.wav') > 5000
    assert len(glob.glob('outputs/figures/*.png')) >= 2
