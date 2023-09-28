#!/bin/bash
# Deploy to executable file on unix

pyinstaller --onefile --windowed --add-data "dataset/*:dataset" src/app/app.py

#need to test on unix machine for deployment
