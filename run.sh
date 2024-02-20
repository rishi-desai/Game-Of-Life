#!/bin/bash

# Use ./run.sh to run main in life.py, use ./run.sh -t
# to run tests in test_life.py

# Parse command line arguments
while getopts ":t" opt; do
    case $opt in
        t)
            # Run tests
            python test_life.py
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            ;;
    esac
done

# Run main function
if [ $OPTIND -eq 1 ]; then
    python life.py
fi
