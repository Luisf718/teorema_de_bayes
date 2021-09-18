# Formula del teorema de Bayes
def calc_bayes(prior_a, prob_b_dado_a, pro_b):
    return (prior_a * prob_b_dado_a) / pro_b

if __name__ == "__main__":

    # Datos para hacer el calculo del teorema de Bayes, calculando la probabilidad de que choques dado que manejes
    prob_choques = 5076 / 731391
    prob_manejes_dado_choques = 5076
    prob_manejes_dado_no_choques = 232924 / 726315
    prob_no_choques = 5076 - prob_choques


    # Calculo la probabilidad de que choques con la formula que dice Bayes para sacar la probabilidad de B
    prob_manejes = (prob_manejes_dado_choques * prob_choques) + (prob_manejes_dado_no_choques * prob_no_choques)

    # Corro la función del teorema de Bayes, para calcular la probabilidad de que choques dado que mueras
    prob_choques_dado_manejes = calc_bayes(prob_choques, prob_manejes_dado_choques, prob_manejes)

    print(prob_choques_dado_manejes)  