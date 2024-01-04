# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(mapoutputs: list) -> dict:

    shuffled_data = {}
    for pair in mapoutputs:
        key, value = pair
        if key not in shuffled_data:
            shuffled_data[key] = []
        shuffled_data[key].append(value)
    
    return shuffled_data