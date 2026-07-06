# Diferença simétrica — o que está em um OU outro, mas não nos dois

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A ^ B              # → {1, 2, 5, 6}
A.symmetric_difference(B)
print(A.symmetric_difference(B))