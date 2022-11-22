#!/usr/bin/env python

import pandas as pd
from pathlib import Path
import sys
import os


def parse_args():
    """
    Function to parse user input in a basic way. Checks number of args
    and stores them to a dictionary
    :param: sys.argv[0] - start date for search (YYYY-MM-DD HH:MM:SSUTC)
    :param: sys.argv[1] - end date for search (YYYY-MM-DD HH:MM:SSUTC)
    :param: sys.argv[2] - path to log file in .txt format
    :return: Returns a dictionary with input params as key value pairs
    """
    if len(sys.argv) < 4:
        print("Copy these args and modify:\n\t\"'2019-03-01 09:00:00UTC' '2019-03-02 11:59:59UTC' './log.txt'?")
        sys.exit()

    if len(sys.argv) > 4:
        print("Copy these args and modify:\n\t\"'2019-03-01 09:00:00UTC' '2019-03-02 11:59:59UTC' './log.txt'?")
        sys.exit()

    args = {}
    args["start"] = str(sys.argv[1])
    args["end"] = str(sys.argv[2])
    args["file_path"] = str(sys.argv[3])

    return args


def read_input_file(file_path: str) -> list:
    """
    Function to read input file in correct folder relative user 
    :param file_path: Filepath in string format ("/log.txt")
    :return: Returns a list where each element is a string line 
    from the file read
    """

    try:
        path = Path.cwd() / file_path
        with open(path) as file:
            data_read = file.readlines()
            return data_read
    except FileNotFoundError:
        raise FileNotFoundError(f"ERROR - File {file_path} does not exist")
    except Exception as error:
        raise error


def structure_data(str_list):
    """
    Clean data and convert string list to a list of 
    dictionaries
    :param: A list of strings read from a log file
    :return: A list of dictionaries where each string
    is a dictionary
    """

    str_list = [line.split("|")[1:4] for line in str_list]
    str_list = [[x.strip() for x in line] for line in str_list]

    # Remove header row from file content list
    str_list.pop(0)

    # Declare new list to append dictionaries to
    dict_list = []

    # Define keys to be used in row dicts
    dict_keys = ["timestamp", "url", "userid"]

    # Iterate file content list, create a dict for each row and append to a new list
    for row in str_list:
        dict_list.append(dict(zip(dict_keys, row)))

    return dict_list


def filter_data(dict_list, start, end):
    """
    Filter out data according to user input
    :param: list of dictionairies where each dict 
    is a row from a log file
    :param: start date for search (YYYY-MM-DD HH:MM:SSUTC)
    :param: end date for search (YYYY-MM-DD HH:MM:SSUTC)
    :return: filtered list with dicts in time interval
    """

    filter_result = []
    for rec in dict_list:
        if rec["timestamp"] >= start and rec["timestamp"] <= end:
            filter_result.append(rec)
    return filter_result


def process_data(dict_list):
    """
    Extract unique urls and calculates views and visitors
    for a given page and stores as dictionairies
    :param: list of dictionairies
    :return: Returns a list with dictionairies containing 
    result for user request
    """

    seen = {}
    for rec in dict_list:
        if rec["url"] not in seen:
            seen[rec["url"]] = [rec["userid"]]
        else:
            seen[rec["url"]].append(rec["userid"])

    result = []
    for key, value in seen.items():
        result.append({"page": key, "views": len(
            value), "visitors": len(set(value))})
    return result


def print_report(dict_list):
    """
    Very basic usage, TBD after upcoming needs
    Create dataframe to present the report and print.
    :param: List of dictionairies with result for user 
    request
    """

    df = pd.DataFrame(data=dict_list)
    print(df)


if __name__ == "__main__":
    # User input
    args = parse_args()
    # Read file
    str_list = read_input_file(args["file_path"])
    # Pre-process data
    dict_list = structure_data(str_list)
    # Filter data according to user search
    filtered_dict_list = filter_data(dict_list, args["start"], args["end"])
    # Calculate views and unique visitors
    result_list = process_data(filtered_dict_list)
    # Print tracking report
    print_report(result_list)
