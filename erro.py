valorreal = float(input("Qual o valor real da carga estrutural em kN?\n"))
valormedido = float(input("Qual o valor medido? \n"))
erroabsoluto = valorreal - valormedido
errorelativo = erroabsoluto / valorreal * 100
print(f"\n\n\nO erro absoluto entre o valor real e o valor medido é de {erroabsoluto}kN \nO erro relativo é de {errorelativo}%\n\n\n")
