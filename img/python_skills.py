#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:24:43 2023

@author: juancarl
"""
import matplotlib.pyplot as plt
import numpy as np

# Define your Python skills and proficiency levels
skills = ["code","fenics", "dolphin", "cashocs", "pandas", "scikit-learn", "PySpark", "numpy", "matplotlib", "seaborn"]
proficiency = [5,5, 4, 4, 5, 4, 3, 4, 4, 3]

# Ensure the number of skills matches the number of proficiency levels
if len(skills) != len(proficiency):
    raise ValueError("Skills and proficiency levels must have the same number of elements")

# Number of skills
num_skills = len(skills)

# Create a list of angles (in radians) for the skills
angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()

# Make a complete circular chart by appending the start skill at the end
skills += [skills[0]]
proficiency += [proficiency[0]]
angles += [angles[0]]

# Create a radar chart
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Fill the area inside the radar chart
ax.fill(angles, proficiency, 'b', alpha=0.2)

# Set radial labels
ax.set_yticklabels(["Novice", "Intermediate", "Proficient", "Advanced", "Expert"], fontsize=14)

# Add skill labels
ax.set_xticks(angles)
ax.set_xticklabels(skills, fontsize=20)

# Rotate the skill labels for better alignment
ax.set_xticklabels(skills, fontsize=20, rotation=45)

# Add a title
#plt.title("Python Skills Radar Chart", fontsize=12)

# Save the chart as an image
plt.savefig("skills_radar_chart.png")

# Show the radar chart
plt.show()
