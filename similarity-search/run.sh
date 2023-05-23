#!/bin/bash

# Get the prompt from command-line arguments
prompt=$1

# Run the Python script with the provided prompt
python main.py --mode test --prompt "$prompt"
