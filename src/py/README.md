# Flower Simulation experiments

## Setup
```Bash
conda create -n "flsim" python=3.9.18
# due to Ubuntu 18.04, installing old version torch
pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116
pip install ray==2.20
pip install -U numpy==1.26.4 # downgrade due to typing deprecation
pip install -U protobuf==4.25.3 grpcio==1.63.0 setuptools==69.5.1 cryptography==42.0.7 tomli==2.0.1 typer==0.12.5 pycryptodome==3.20.0 iterators==0.2.0 datasets==2.19.1 flwr_datasets==0.1.0
```

## Run Simulation
```Bash
python sim.py --num_cpus 4 --num_gpus 1.0
```