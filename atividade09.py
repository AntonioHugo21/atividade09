# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).

q_litros = int(input("digite a quantidade de litros"))
q_quilometros = int(input("digite a quantidade de quilômetros"))

c_medio = q_quilometros/q_litros

print(f"o valor do consumo é = {c_medio}")