# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import azure.functions as func

def main(keyvaluepairs: func.InputStream) -> func.InputStream:

    word_counts = []

    for word, counts in keyvaluepairs.items():
        total_count = sum(counts)
        word_count_dict = {"Word": word, "Count": total_count}
        word_counts.append(word_count_dict)
    return word_counts




