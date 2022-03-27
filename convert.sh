#!/bin/bash
# Clear proc subdirs
rm -rf ./proc/*
# Run conversion script
pipenv run python textify.py
