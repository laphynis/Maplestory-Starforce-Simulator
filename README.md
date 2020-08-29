# Maplestory-Starforce-Simulator
A simple script that simulates starforcing in Maplestory. You can select how many trials to run and the script will output the average meso cost.

This script runs through the passFail.py file. You can choose to run one trial with the experimentalTrial function or many trials with the manyTrials function. However, be wary that selecting too high of a starforce level can cause an error due to memory overflow as this script uses recursion where it can iterate over thousands of times before stopping. Going beyond 22 stars will cause overflow and should be avoided because of how unrealistic it is. 
