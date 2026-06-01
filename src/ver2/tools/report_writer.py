
import os
import datetime


def save_report(content):

    os.makedirs(
        "report/react_agent",
        exist_ok=True
    )

    timestamp = datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"report/individual_reports/agent_{timestamp}.txt"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)

    return filename