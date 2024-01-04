# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import azure.functions as func

def main(line1: tuple) -> list:
    if len(line1) > 1 and isinstance(line1[1], str):
        word_count_pairs = []
        line = line1[1]
        words = line.split()

        for word in words:
            word_count_pairs.append((word, 1))

        return word_count_pairs

    return []