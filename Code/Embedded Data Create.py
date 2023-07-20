#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 00:06:37 2023

@author: smitesh22
"""

import torch
import torch.nn as nn
from AutoEncoder import AutoEncoder

model = AutoEncoder()

weights = torch.load('DEM_model_weights.pt')

model.load_state_dict(weights)

load = torch.load("/home/smitesh22/Data/DEM_slope_tensorv2.pt")

embedded_dict = {}

for data in load:
    embedded_dict[data] = model.encoder(load[data].float())
    print("one dones")