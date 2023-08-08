#!/bin/bash

start_time=$(date +%s)  # Record the start time

python3 sync.py

end_time=$(date +%s)    # Record the end time
execution_time=$((end_time - start_time))  # Calculate the execution time in seconds

echo "The program took $execution_time seconds to run."
