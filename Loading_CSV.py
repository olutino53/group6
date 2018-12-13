#!/usr/bin/env python3

import pandas as pd
import sys


#loading all csv files into dataframes

#add the file to 'edit configurations...' in 'run' so it is used as an argument
#Saagar Mehta
class dataset():
    def main(self):
        inputfile = sys.argv[1]
        d = pd.read_csv(inputfile)
        df = pd.DataFrame(d)
        print(df)


if __name__ == "__main__":
    graph = dataset()
    print(graph.main())


