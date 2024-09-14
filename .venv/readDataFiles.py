import json
import numpy as np
import os

def readDataFiles():
    base_path = os.path.dirname(__file__)
    node_resistances_path = os.path.join(base_path, 'node_resistances.json')
    node_voltages_path = os.path.join(base_path, 'node_voltages.json')

    with open(node_resistances_path, 'r') as file:
        node_resistances = json.load(file)

    with open(node_voltages_path, 'r') as file:
        node_voltages = json.load(file)
        
        
    node_resistances = [[entry['node1'], entry['node2'], entry['resistance']] for entry in node_resistances]
    node_voltages = [[entry['node'], entry['voltage']] for entry in node_voltages]

    return node_resistances, node_voltages

def createMatrix_A(node_resistances, node_voltages):
    matrix_A = np.zeros((25, 25))
    i = 0
    for data in node_resistances:
        node1 = data[0]
        node2 = data[1]
        resistance = data[2]
        V_node1 = 1/resistance
        V_node2 = -1/resistance
        matrix_A[i][node1-1] = V_node1
        matrix_A[i][node2-1] = V_node2
        if i < len(matrix_A)-1:
            i = i+1
    return matrix_A
matrix_B = np.zeros((25,1))

node_resistances, node_voltages = readDataFiles()
matrix_A = createMatrix_A(node_resistances, node_voltages)

print("Matrix A:")
for row in matrix_A:
    print(row)