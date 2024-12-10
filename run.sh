#!/bin/bash

if command -v python3 &>/dev/null; then
    PYTHON=python3
else
    PYTHON=python
fi

$PYTHON app/main.py