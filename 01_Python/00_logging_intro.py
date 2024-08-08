import pandas as pd


def pipeline():
    print("Pipeline started")
    print("Reading data")
    try:
        df: pd.DataFrame = pd.read_csv("./data.csv")
    except FileNotFoundError:
        print("Data not found in original location trying backup location")
        try:
            df: pd.DataFrame = pd.read_csv("./01_Python/data.csv")
        except FileNotFoundError:
            print("Data not found in backup location")
            return
    print("Data read")
    print("Processing data")
    df["processed_A"] = df["A"] + 1
    print("Data processed")
    print("Writing data")
    df.to_csv("./output.csv")
    print("Data written")
    print("Pipeline finished")


if __name__ == "__main__":
    pipeline()
