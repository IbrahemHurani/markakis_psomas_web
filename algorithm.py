from fairpyx import Instance, divide
from fairpyx.algorithms.markakis_psomas import algorithm1_worst_case_allocation
from io import StringIO
import logging

def run_algorithm(valuations):
    # איסוף לוגים מהאלגוריתם
    log_stream = StringIO()
    logger = logging.getLogger("fairpyx.algorithms.markakis_psomas")
    logger.setLevel(logging.INFO)

    # הוספת handler חדש אם לא קיים
    if not any(isinstance(h, logging.StreamHandler) and h.stream == log_stream for h in logger.handlers):
        stream_handler = logging.StreamHandler(log_stream)
        stream_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    instance = Instance(valuations=valuations)
    allocation = divide(algorithm=algorithm1_worst_case_allocation, instance=instance)

    result_values = {}
    for agent in allocation:
        result_values[agent] = sum(valuations[agent][item] for item in allocation[agent])

    log_stream.seek(0)
    logs = log_stream.read().splitlines()

    return allocation, result_values, logs
