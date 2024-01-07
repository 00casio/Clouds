# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    fake_input = [
        (1, "hello how are you is everything good hamza hamza"),
        (2, "we where doing all this in a short time hello what are you good we in good hamza"),
        (3, "hamza hamza hamza hanza hanza hamzaa"),
        (4, "hamza hamza hamza a, a,")
    ]
    filenames = ["mrinput-1.txt", "mrinput-2.txt", "mrinput-3.txt", "mrinput-4.txt"]
    input_data = yield context.call_activity("getiputdatafn", filenames)

    map_tasks = []
    for data in input_data:
        map_tasks.append(context.call_activity('Map', data))
    
    map_results = yield context.task_all(map_tasks)
   
    shuffled_data = yield context.call_activity('Shuffler',map_results)

    reducer_tasks = []
    for data in shuffled_data.values():
        reducer_tasks.append(context.call_activity('Reducer', data))

    reduced_data = yield context.task_all(reducer_tasks)
    return reduced_data


main = df.Orchestrator.create(orchestrator_function)
