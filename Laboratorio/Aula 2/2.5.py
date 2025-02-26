alturad=float(input("\n\tInsira a altura do degrau em centimetros:"))
alturac=float(input("\n\tInsira a altura desejada a chegar em metros:"))
alturac=alturac*100
degraus=(alturac//alturad)+1
print("\n\t A quantidade de degrais {:2}".format(degraus))