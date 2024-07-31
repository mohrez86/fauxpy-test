#! /usr/bin/env bash

# Time to run on my machine: 10230.746402 seconds.

# Exiting when any command fails
set -e

# Parameters
SCRIPTS_DIR_NAME="scripts_tiny"

# Running
TIMER_START="$EPOCHREALTIME"
cd "$SCRIPTS_DIR_NAME"

for bash_script in $(find . -name "*.sh" -type f); do
    echo "==============================================="
    echo "Running $bash_script"
    echo "==============================================="
    "$bash_script"
done

TIMER_STOP="$EPOCHREALTIME"
TIMER_ELAPSED=$(bc -l <<< "$TIMER_STOP - $TIMER_START")
echo "Elapsed time (seconds): $TIMER_ELAPSED"
