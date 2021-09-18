# Formula del teorema de Bayes
def calc_bayes(prior_a, prob_b_dado_a, pro_b):
    return (prior_a * prob_b_dado_a) / pro_b

if __name__ == "__main__":

    # Datos para hacer el calculo del teorema de Bayes, calculando la probabilidad de que mueras dado que choques

    prob_muerte = 27 / 731391 
    prob_choques_dado_mueres = 27 
    prob_choques_dado_no_mueras = 5049 / 731364 
    prob_no_mueras = 27 - prob_muerte

    # Calculo la probabilidad de que choques con la formula que dice Bayes para sacar la probabilidad de B
    prob_choques = (prob_choques_dado_mueres * prob_muerte) + (prob_choques_dado_no_mueras * prob_no_mueras)

    # Corro la función del teorema de Bayes, para calcular la probabilidad de que mueras dado que choques
    prob_mueras_dado_choques = calc_bayes(prob_muerte, 
    prob_choques_dado_mueres, prob_choques)

    print(prob_mueras_dado_choques)
    