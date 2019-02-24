# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
train_2mb = dataiku.Dataset("train_2mb")
train_2mb_df = train_2mb.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

pyout_df = train_2mb_df # For this sample code, simply copy input to output


# Write recipe outputs
pyout = dataiku.Dataset("pyout")
pyout.write_with_schema(pyout_df)
