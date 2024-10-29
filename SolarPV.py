#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:51:36 2024

@author: mercy
"""

import math

# User input
building_width = float(input("Enter building width (m): ")) #shorter side
building_length = float(input("Enter building length (m): ")) #longer side
roof_angle = float(input("Enter roof angle (deg): "))
pv_width_mm = float(input("Enter PV panel width (mm): ")) #longer side
pv_height_mm = float(input("Enter PV panel height (mm): ")) #shorter side
pv_power = float(input("Enter PV panel power (Wp): "))

# Convert angles and dimensions
roof_angle_rad = math.radians(roof_angle)  # Convert angle to radians for trigonometric functions
roof_length_m = building_length #longer side
roof_width_m = building_width / (2 * math.cos(roof_angle_rad)) #shorter side

pv_width = pv_width_mm / 1000    # Convert mm to m #longer side
pv_height = pv_height_mm / 1000  # Convert mm to m #shorter side

# Calculate the number of panels that can fit 
max_panels_long = math.floor(roof_length_m / pv_width) #longer side
max_panels_short = math.floor(roof_width_m / pv_height) #shorter side
max_num_panels = max_panels_long * max_panels_short * 2 #panels on 2 sides

# Calculate the total power capacity
total_capacity_kWp = pv_power * max_num_panels/1000

# Return the results
print(f"Maximum number of solar panels: {max_num_panels}")
print(f"Total power capacity (kWp): {total_capacity_kWp}")