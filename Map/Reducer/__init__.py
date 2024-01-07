# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import azure.functions as func

def main(keyvaluepairs: func.InputStream) -> func.InputStream:

    reduced_data = {}
    for word, count in keyvaluepairs:
        if word in reduced_data:
            reduced_data[word] += count
        else:
            reduced_data[word] = count

    return reduced_data




