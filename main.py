import pandas as pd
import numpy as np


def main():
    disp_df = pd.read_csv("disp_st6ns1.txt.bz2", compression="bz2", index_col=0)
    comp_df = pd.read_csv("disp_st6ns1.txt.bz2", compression="bz2", index_col=0)

    train_disp_df = disp_df[0:3650]
    test_disp_df = disp_df[3651:]

    train_comp_df = comp_df[0:3650]
    test_comp_df = comp_df[3651:]

    print(disp_df)
    #print("\n")
    #print(comp_df)

main()