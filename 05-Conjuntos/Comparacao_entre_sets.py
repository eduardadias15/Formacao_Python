A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

A.issubset(B)      # A ⊆ B? → True
B.issuperset(A)    # B ⊇ A? → True
A.isdisjoint(B)    # Sem elementos em comum? → False