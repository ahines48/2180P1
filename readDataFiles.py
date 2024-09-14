import json

def readDataFiles():
    with open('node_resistance.json', 'r') as file:
        node_resistances = json.load(file)

    with open('node_voltages.json', 'r') as file:
        node_voltages = json.load(file)
        
    node_resistances = [[entry['node1'], entry['node2'], entry['resistance']] for entry in node_resistances]
    node_voltages = [[entry['node'], entry['voltage']] for entry in node_voltages]

    return node_resistances, node_voltages

def createMatrix_A(node_resistances, node_voltages):
    matrix_A = [[0 for i in range(5)] for j in range(5)]
    for data_resistances in node_resistances:
        node1 = data_resistances[0]
        node2 = data_resistances[1]
        resistance = data_resistances[2]
        entry = node1 - node2
       
    for data_voltages in node_voltages:
        node = data_voltages[0]
        voltage = data_voltages[1]
    
    for k in range(len(len(matrix_A))):
         for l in range(len(matrix_A))
         matrixA[k][]
         if node_resistances[k][0] or node_resistances[k][1] == node_voltages[0][0] or node_voltages[1][0]:
             skip
        else:
            matrixA[k][]
    return matrix_A