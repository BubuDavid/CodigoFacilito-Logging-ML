from datetime import datetime

import pandas as pd


def logging(msg: str) -> None:
    current_time = datetime.now()
    time_formatted = current_time.strftime("%Y-%m-%d %H:%M:%S")
    # Basic with time
    print(f"[{time_formatted}] - {msg}")
    # How to put the file name?
    # print(f"[{time_formatted}|{__file__.split('/')[-1].replace(r'.py', '')}] - {msg}")
    # How to put the function name?
    # print(
    #     f"[{time_formatted}|{__file__.split('/')[-1].replace(r'.py', '')}|{logging.__name__}] - {msg}"
    # )  # mmhhhhh


def pipeline():
    logging("Pipeline started")
    logging("Reading data")
    try:
        df: pd.DataFrame = pd.read_csv("./data.csv")
    except FileNotFoundError:
        logging("Data not found in original location trying backup location")
        try:
            df: pd.DataFrame = pd.read_csv("./01_Python/data.csv")
        except FileNotFoundError:
            logging("Data not found in backup location")
            return
    logging("Data read")
    logging("Processing data")
    df["processed_A"] = df["A"] + 1
    logging("Data processed")
    logging("Writing data")
    df.to_csv("./output.csv")
    logging("Data written")
    logging("Pipeline finished")


if __name__ == "__main__":
    pipeline()
