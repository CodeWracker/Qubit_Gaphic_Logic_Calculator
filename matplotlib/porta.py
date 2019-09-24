def portaX(qubit):
    aux = qubit[2]
    aux2 = qubit[3]
    qubit[2] = qubit[0]
    qubit[3] = qubit[1]
    qubit[0] = aux
    qubit[1] = aux2
    return qubit
    