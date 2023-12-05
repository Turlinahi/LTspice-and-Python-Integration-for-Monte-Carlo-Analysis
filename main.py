import subprocess
import openpyxl
import numpy as np
import os

def run_ltspice(netlist_path):
    ltspice_path = r'C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe'
    subprocess.run([ltspice_path, '-b', '-ascii', netlist_path])

def extract_values_from_log(log_path):
    with open(log_path, 'r') as log_file:
        lines = log_file.readlines()

        vb_value, va_value = None, None

        for line in reversed(lines):
            if 'vb_bf' in line:
                vb_value = extract_value_from_line(line)
            elif 'va_bf' in line:
                va_value = extract_value_from_line(line)

            if vb_value is not None and va_value is not None:
                break

        return va_value, vb_value


def extract_value_from_line(line):
    try:
        value_str = line.split('=')[1].strip()
        value = float(value_str)
        return value
    except (IndexError, ValueError):
        return None


def calculate_mean_and_variance(values):
    mean = np.mean(values)
    variance = np.var(values)
    return mean, variance

def write_to_excel(output_excel, va_values, vb_values, mean_va, var_va, mean_vb, var_vb):
    wb = openpyxl.Workbook()
    ws = wb.active

    # Write headers
    ws.append(['Sample', 'VA', 'VB'])

    # Write data
    for i, (va, vb) in enumerate(zip(va_values, vb_values), start=1):
        ws.append([i, va, vb])

    # Write statistics
    ws.append([])  # Empty row for better readability
    ws.append(['Mean', mean_va, mean_vb])
    ws.append(['Variance', var_va, var_vb])

    # Save Excel file
    wb.save(output_excel)

    # Open Excel file with the default application
    os.system(f'start excel "{output_excel}"')

def main():
    netlist_path = r'C:\Users\ioana\OneDrive\Documents\LTspiceXVII\Monte_Carlo_Memory_Cell.asc'
    log_path = r'C:\Users\ioana\OneDrive\Documents\LTspiceXVII\Monte_Carlo_Memory_cell\Monte_Carlo_Memory_Cell.log'
    output_excel = r'C:\Users\ioana\OneDrive\Documents\LTspiceXVII\Monte_Carlo_Memory_cell\output_data.xlsx'
    num_samples = 10

    all_va_values = []
    all_vb_values = []

    for sample in range(1, num_samples + 1):
        run_ltspice(netlist_path)
        va_value, vb_value = extract_values_from_log(log_path)
        all_va_values.append(va_value)
        all_vb_values.append(vb_value)

    mean_va, var_va = calculate_mean_and_variance(all_va_values)
    mean_vb, var_vb = calculate_mean_and_variance(all_vb_values)

    write_to_excel(output_excel, all_va_values, all_vb_values, mean_va, var_va, mean_vb, var_vb)

if __name__ == "__main__":
    main()
