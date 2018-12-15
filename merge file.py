#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt  # added plotly function for bar graph
from matplotlib import style
import csv
import sys

# Load the CSV file into a dataframe
def main():
    global project_df
    inputfile = sys.argv[1]
    project_df = pd.read_csv(inputfile, low_memory= False)


class states():
    def compare_any50(self):

        # Load the CSV file into a dataframe
        project_df.dtypes  # confirms what each column type is
        # print(project_df.dtypes)

        # tells number of rows, then columns
        print('There are', project_df.shape[0], 'Rows', '\nAnd', project_df.shape[1], 'Columns')

        # setting the code indexed by state
        firstAnalysis_df = project_df
        secondConfigure_df = project_df

        # extracts first 52 rows and first 12 columns to shorten the huge csv
        # shows needed rows and columns but also saves the changes made as firstcode_df
        firstAnalysis_df = firstAnalysis_df.iloc[:52, :12]

        # print(firstAnalysis_df)

        first_df = firstAnalysis_df  # set up temporary dataframe to avoid losing any progress here on out

        ###firstcode_df.drop(['Guam', 'Puerto Rico'])
        first_df = first_df.drop(first_df.index[10])  # removes guam and puerto rico
        first_df = first_df.drop(first_df.index[38])

        firstAnalysis_df = first_df  # return to original data frame
        firstAnalysis_df = firstAnalysis_df.sort_values(by='LocationDesc')

        # sets LocationDesc, the state names, as index
        firstAnalysis_df.set_index('LocationDesc', inplace=True)
        # print(firstAnalysis_df)

        states_list = firstAnalysis_df.index.values.tolist()  # creats a dictionary of all the states/abbr for later use of order
        print("List of States:")
        for state in states_list:
            print(state)

        # print('this is a list of the states', states_list)


    # compares rates of alcohol use among youth in any two of the 50 states that the user chooses.

        print(
            'Select two states to compare their rates at which alcohol is used among youth. Please use correct capitalization.')
        ## a test code can be written for user that input an invalid state.
        state_1 = input('Pick one state:')
        state_2 = input('Pick another state:')
        if state_1 in states_list and state_2 in states_list:  # added states_list in front of state_1
            value_1 = firstAnalysis_df.loc[state_1, 'DataValueAlt']
            value_2 = firstAnalysis_df.loc[state_2, 'DataValueAlt']

            print("Percent of alcohol use among youth in " + state_1 + ": " + str(value_1))
            print("Percent of alcohol use among youth in " + state_2 + ": " + str(value_2))

            if pd.isnull(value_1) and pd.isnull(value_2):
                print("Both states you have entered do not have a recorded percent frequency of alcohol use among youth.")
            elif pd.isnull(value_1):
                print("The first state you entered does not have a recorded percent frequency of alcohol use among youth.")
            elif pd.isnull(value_2):
                print("The second state you entered does not have a recorded percent frequency of alcohol use among youth.")
            else:
                if value_1 > value_2:
                    print(state_1 + " has a greater percent frequency of alcohol use among youth than " + state_2)
                else:
                    print(state_2 + " has a greater percent frequency of alcohol use among youth than " + state_1)

            ##Creating a bar chart to comapare the two different states
            ##comparing the rates of alcohol use among youths in two states
            print("Value of state one:", value_1)
            print("Value of state two:", value_2)
            x = value_1
            y = value_2
            plt.bar(x, label='Graph', color='red', height=x)
            plt.bar(y, color='blue', height=y)
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.title('Bar Graph on rates of alcohol use for\n' + state_1 + ' and ' + state_2)
            plt.show()
        else:
            print("Please input valid states in the U.S. with correct spelling and capitalization")

# def test():
#     assert


if __name__ == '__main__':
    main()
    state = states()
    print(state.compare_any50())
