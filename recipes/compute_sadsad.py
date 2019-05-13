# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
train_2mb_prepared = dataiku.Dataset("train_2mb_prepared")
train_2mb_prepared_df = train_2mb_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

sadsad_df = train_2mb_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
sadsad = dataiku.Dataset("sadsad")
sadsad.write_with_schema(sadsad_df)
