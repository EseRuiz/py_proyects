def proverb(*prover ,qualifier):
    out = []
    if prover == ():
        return []
    for i in range(len(prover)-1):
        out.append(f"For want of a {prover[i]} the {prover[i+1]} was lost.")
    if qualifier == None:
        out.append(f"And all for the want of a {prover[0]}.")
    else:
        out.append(f"And all for the want of a {qualifier} {prover[0]}.")
    return (out)

input_data = ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]
a = proverb(*input_data, qualifier="horseshoe")
print(a)