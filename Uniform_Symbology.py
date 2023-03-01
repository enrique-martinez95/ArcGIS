# Author: Enrique Martinez
# This function is designed to apply the same symbology to multiple feature classes using a layer style file
# This is similar to the batch symbology function however the data do not need to be added to the data frame first
# The function will apply the symbology directly to the feature classes and then add them to the data frame


# Import libraries
# tk is imported to add a GUI for selecting inputs

import arcpy
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Get the folder containing shapefiles and their subfolders

folder_path = filedialog.askdirectory(title="Select folder containing shapefiles")

# Get the path to the .lyrx file

lyrx_path = filedialog.askopenfilename(title="Select .lyrx file")

# Define the function to apply symbology to shapefiles

def apply_symbology(shapefile_path, lyrx_path):
    arcpy.management.ApplySymbologyFromLayer(shapefile_path, lyrx_path)

# Walk through the folder and subfolders, and apply symbology to each shapefile

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".shp"):
            shapefile_path = os.path.join(root, file)
            apply_symbology(shapefile_path, lyrx_path)

print("Feature classes succesfully symbolized")



