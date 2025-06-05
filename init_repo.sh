#!/usr/bin/env bash
set -e

# create structure
mkdir -p stimuli experiment analysis figures manuscript notebooks capsule

# python env
python3 -m venv .venv
source .venv/bin/activate

# requirements file
cat << 'REQ' > requirements.txt
jsPsych==7.3.1
pymc==5.15.0
arviz==0.18.0
jupyterlab==4.2
matplotlib==3.9.0
pandas==2.2.2
numpy==2.0.0
pingouin==0.5.4
REQ

# licence
curl -s https://www.gnu.org/licenses/gpl-3.0.txt > LICENSE

# git init
git init -q
git add .
git commit -qm "Initial scaffold"

echo "✅ MoralBayes scaffold ready"
