"""
Processing data on nuclear binding energy in order to create a plot
"""
import pandas as pd


def process_data():
    df = pd.read_csv(r"nuclear-binding-energy.csv", sep=" ", names=["mass number", "proton number", "isotope", "mass", "binding energy", "binding energy per nucleon"], index_col=False)
    df.to_csv("processed-binding-energy.csv",columns=["mass number", "binding energy per nucleon"], index=False, sep=" ")

def main():
    process_data()


if __name__ == "__main__":
    main()