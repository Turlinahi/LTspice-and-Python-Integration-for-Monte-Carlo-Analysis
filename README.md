
# LTspice and Python Integration for Monte Carlo Analysis




https://github.com/Turlinahi/LTspice-and-Python-Integration-for-Monte-Carlo-Analysis/assets/133703884/64c385cd-516b-44f5-85cb-f66eda7b44da




## Overview

This repository contains Python scripts that integrate with LTspice for performing Monte Carlo analysis on a memory cell circuit. The circuit, implemented in LTspice, utilizes a Monte Carlo sweep for the transistor model parameters.

![image](https://github.com/Turlinahi/LTspice-and-Python-Integration-for-Monte-Carlo-Analysis/assets/133703884/7659ce5b-a687-43a8-afeb-3a3239c2271f)

## Features

- **LTspice Circuit:** The LTspice circuit (`Monte_Carlo_Memory_Cell.asc`) includes a memory cell implemented with transistors and model parameter variations using Monte Carlo analysis.

- **Python Script (`main.py`):**
  - **Run LTspice Simulations:** Utilizes the subprocess module to run LTspice simulations from Python.
  - **Extract Simulation Results:** Parses the LTspice log files to extract key values such as V(va), V(vb), and BF.
  - **Data Analysis:** Calculates mean and variance of V(va) and V(vb) for multiple Monte Carlo samples.
  - **Excel Output:** Writes the results, including Va and Vb values, mean, and variance, to an Excel file.
 
    ![image](https://github.com/Turlinahi/LTspice-and-Python-Integration-for-Monte-Carlo-Analysis/assets/133703884/27d5086d-3d29-49fa-9f08-1dabd302bfa0)


## How to Use

1. **LTspice Simulation:**
   - Open and run the LTspice circuit (`Monte_Carlo_Memory_Cell.asc`).
   - Ensure LTspice is installed in the default path or update `ltspice_path` in `main.py` accordingly.

2. **Python Script:**
   - Run `main.py` to perform Monte Carlo analysis, extract values, and save results in an Excel file.

3. **Dependencies:**
   - Python 3
   - Required Python packages: `subprocess`, `openpyxl`, `numpy`

## Notes

- The LTspice circuit includes a Monte Carlo sweep for the 2N2222 transistor model parameters.

- The Python script automates LTspice simulations, extracts relevant data, and performs basic data analysis.

Feel free to explore and contribute to further enhance the integration between LTspice and Python for circuit analysis.
![image](https://github.com/Turlinahi/LTspice-and-Python-Integration-for-Monte-Carlo-Analysis/assets/133703884/b7a97eb5-7dcc-45b2-8a8d-1d81845b3b44)
![image](https://github.com/Turlinahi/LTspice-and-Python-Integration-for-Monte-Carlo-Analysis/assets/133703884/a24851a5-4ab6-4531-8d60-36f15ceb7563)


