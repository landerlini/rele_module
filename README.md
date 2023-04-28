# Rele Module controller

This package implements a super-simplified REST-based interface for the 
8CH RELE MODULE developed by Roberto Ciaranfi at INFN Firenze.

## Installation
We recommend using conda.
```bash
conda create -n rele_module
conda activate rele_module
conda install ftd2xx
pip install uvicorn fastapi
git clone https://github.com/landerlini/rele_module.git -o rele_module
python -m uvicorn main:app --reload
```

## Controlling
From a browser visit the URL
```bash
localhost:8000/set?q=<binary_number>
```
replacing `"binary_number"` with a string of 8 digits (0 or 1).
For example,
 - `10000000` switches on the relais corresponding to the most significant bit
 - `00000001` switches on the relais corresponding to the least significant bit
 - `11111111` switches on the relais corresponding to the least significant bit
 - `00000000` switches off the relais corresponding to the least significant bit
