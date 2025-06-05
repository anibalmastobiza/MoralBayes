#!/usr/bin/env bash
set -e
source .venv/bin/activate
python stimuli/make_stimuli.py
jupyter nbconvert --execute notebooks/power_analysis.ipynb --to html --output notebooks/power_analysis_out.html
jupyter nbconvert --execute analysis/model_fit.ipynb --to html --output analysis/model_fit_out.html || true
latexmk -pdf -quiet manuscript/paper.tex
echo "🎉 Pipeline complete"
