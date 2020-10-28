#!/usr/bin/env bash

# Install dllib
git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build
cd build
cmake ..
cmake --build .
cd ..
python3 setup.py install
# Install All python packages
cd ..
pip install -r ../requirements.txt
# Download weights for Yolo3
bash models/yolo3/weights/download_weights.sh
