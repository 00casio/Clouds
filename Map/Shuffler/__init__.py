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
    for sentence in mapoutputs:
        for words in sentence:
            if len(words) == 2:
                word, count = words
                if word not in shuffled_data:
                    shuffled_data[word] = []
                shuffled_data[word].append((word, count))
            else: 
                for word, count in words:
                    if word not in shuffled_data:
                        shuffled_data[word] = []
                    shuffled_data[word].append((word, count))

    return shuffled_data