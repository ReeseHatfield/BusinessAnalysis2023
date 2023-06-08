#!/bin/bash

pyinstaller --onefile --windowed --add-data "dataset/*:dataset" src/app/app.py

#need to test on unix machine for deployment