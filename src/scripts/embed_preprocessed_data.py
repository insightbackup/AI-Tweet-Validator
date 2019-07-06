#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Takes filtered user tweet files from 'preprocessed_data_path', generates
embeddings, and writes output processed_data_path.

June, 2019
@author: Joshua Rubin
"""

import os
from get_config import get_config
from tweetvalidator.data_processing import embed_tweets_from_directories

config = get_config()

input_directory = config['preprocessed_data_path']
output_directory = config['processed_data_path']

if not os.path.isdir(output_directory):
    print(f"Path doesn't exist; creating {output_directory}.")
    os.makedirs(output_directory)

embed_tweets_from_directories(input_directory, 
                              output_directory)
                              