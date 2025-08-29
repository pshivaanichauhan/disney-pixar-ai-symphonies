.PHONY: mid xml wav plots all test

mid:
	python ml_style/infer.py --out outputs/score.mid

xml: mid
	python rpa_orchestration/build_parts.py --in outputs/score.mid --out outputs/score.musicxml

wav: mid
	python oop_counterpoint/render_audio.py --in outputs/score.mid --out outputs/audio_preview.wav

plots: xml
	python cv/plots.py --in outputs/score.musicxml --out outputs/figures

all: mid xml wav plots

test:
	pytest -q --maxfail=1 --disable-warnings
