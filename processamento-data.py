import pandas
import statistics
import matplotlib.pyplot as plot

# Questão 1
data = pandas.read_csv("dados4.csv")
idadesValidas = data['age'].dropna()
moda = statistics.mode(idadesValidas)

data['age'].fillna( moda, inplace=True)

with open("Resposta1.txt", "w") as f:
    f.write(data.to_string(index=False))

# Questão 2
count = data['sex'].value_counts()
homens = count["male"]
mulheres = count["female"]

print(f'Numero de homens: { homens }')
print(f'Numero de mulheres: { mulheres }')
print(f'Numero de homens e mulheres: { homens + mulheres }')

# Questão 3
sobrevivente = data['survived'].value_counts()

plot.figure(figsize=(8, 8))
plot.pie( sobrevivente, labels=['sobrevivente', 'vitima'], autopct='%1.1f%%')
plot.title('Sobreviventes e Vítimas')
plot.savefig("grafico.png")

# Questão 4
plot.clf()

idade = data['age']
tarifa = data['fare']

plot.scatter( idade, tarifa)

plot.xlabel('Idade')
plot.ylabel('Tarifa')

plot.title('Dispersão: Idade por Tarifa')

plot.show()