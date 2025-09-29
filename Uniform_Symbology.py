# Author: Enrique Martinez
# This function applies a uniform symbology to all feature classes in a target folder and adds them to a data frame.
# This is ideal when an organization requires a consistent design language among GIS users.
# I created a similar script while working for SeekOps Inc. to automate our symbology workflow, reducing turnaround by 80%


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




