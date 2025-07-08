
def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) e retorna a classificação.

    Args:
        peso (float): O peso da pessoa em quilogramas (kg).
        altura (float): A altura da pessoa em metros (m).

    Returns:
        str: A classificação do IMC.
    """
    if not isinstance(peso, (int, float)) or not isinstance(altura, (int, float)):
        return "Erro: Peso e altura devem ser números."
    if altura <= 0 or peso <= 0:
        return "Erro: Peso e altura devem ser valores positivos."

    try:
        imc = peso / (altura ** 2)
    except ZeroDivisionError:
        return "Erro: A altura não pode ser zero."

    if imc < 18.5:
        return "baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "peso adequado"
    elif 25.0 <= imc <= 29.9:
        return "sobrepeso,é recomendado consultar um médico"
    elif 30.0 <= imc <= 34.9:
        return "obesidade grau I,é recomendado consultar um médico"
    elif 35.0 <= imc <= 39.9:
        return "obesidade grau II,é recomendado consultar um médico"
    else:  # imc >= 40.0
        return "obesidade grau III,é recomendado consultar um médico"

if __name__ == "__main__":
    print("Bem-vindo(a) ao Calculador de IMC!")
    print("----------------------------------")

    while True:
        try:
            peso_str = input("Digite seu peso em kg (ex: 70.5): ").replace(',', '.')
            peso = float(peso_str)

            altura_str = input("Digite sua altura em metros (ex: 1.75): ").replace(',', '.')
            altura = float(altura_str)

            if altura == 0:
                print("Erro: A altura não pode ser zero. Por favor, digite um valor válido.")
                continue

            resultado = calcular_imc(peso, altura)
            print(f"\nSeu IMC é: {peso / (altura ** 2):.2f}")
            print(f"Classificação: {resultado}")
            break # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números para peso e altura.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    print("\nObrigado por usar o Calculador de IMC!")