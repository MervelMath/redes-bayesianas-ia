from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

modelo_seguranca = BayesianNetwork( [
          ('Autenticacao','Tupla'),
          ('Autenticacao','Biometria'),
          ('Autenticacao','Propriedade'),
          ('Tupla','Atualizacao'),
          ('Tupla','CaseSensitive'),
          ('Tupla','Alfanumerico'),
          ('Tupla','MinimoCaracteres'),
          ('Tupla','CaractereEspecial')
         ]
        )

#region tabelas
autenticacao_cpd = TabularCPD(
    variable = 'Autenticacao',
    variable_card = 3,
    values=[[0.2], [0.5],[0.3]],
    state_names={"Autenticacao": ["Forte", "Medio", "Fraco"]}
)
# print(autenticacao_cpd)

tupla_cpd = TabularCPD(
    variable='Tupla',
    variable_card=3,
    values=[[0.2, 0.2, 0.2], [0.5, 0.5, 0.5], [0.3, 0.3, 0.3]],
    evidence_card=[3],
    evidence=['Autenticacao'],
    state_names={"Tupla": ["Forte", "Medio", "Fraco"], 'Autenticacao':["Forte", "Medio", "Fraco"]}
    )
# print(tupla_cpd)

atualizacao_cpd = TabularCPD(
    variable = 'Atualizacao',
    variable_card = 2,
    values=[[0.8, 0.6, 0.4], [0.2, 0.4,0.6]],
    evidence_card = [3],
    evidence=['Tupla'],
    state_names={"Atualizacao": ["Sim", "Nao"], 'Tupla':["Forte", "Medio", "Fraco"]}
    )
# print(atualizacao_cpd)

case_sensitive_cpd = TabularCPD(
    variable = 'CaseSensitive',
    variable_card = 2,
    values=[[0.8, 0.6, 0.4], [0.2, 0.4,0.6]],
    evidence_card = [3],
    evidence=['Tupla'],
    state_names={"CaseSensitive": ["Sim", "Nao"], 'Tupla':["Forte", "Medio", "Fraco"]}
    )
# print(case_sensitive_cpd)

alfanumerico_cpd = TabularCPD(
    variable = 'Alfanumerico',
    variable_card = 2,
    values=[[0.8, 0.6, 0.4], [0.2, 0.4,0.6]],
    evidence_card = [3],
    evidence=['Tupla'],
    state_names={"Alfanumerico": ["Sim", "Nao"], 'Tupla':["Forte", "Medio", "Fraco"]}
    )
# print(alfanumerico_cpd)

minimo_caracteres_cpd = TabularCPD(
    variable = 'MinimoCaracteres',
    variable_card = 2,
    values=[[0.8, 0.6, 0.4], [0.2, 0.4,0.6]],
    evidence_card = [3],
    evidence=['Tupla'],
    state_names={"MinimoCaracteres": ["Sim", "Nao"], 'Tupla':["Forte", "Medio", "Fraco"]}
    )
# print(minimo_caracteres_cpd)

caractere_especial_cpd = TabularCPD(
    variable = 'CaractereEspecial',
    variable_card = 2,
    values=[[0.8, 0.6, 0.4], [0.2, 0.4,0.6]],
    evidence_card = [3],
    evidence=['Tupla'],
    state_names={"CaractereEspecial": ["Sim", "Nao"], 'Tupla':["Forte", "Medio", "Fraco"]}
    )
# print(caractere_especial_cpd)

biometria_cpd = TabularCPD(
    variable = 'Biometria',
    variable_card = 5,
    values=[[0.2, 0.2, 0.2], [0.1, 0.5,0.2],[0.05, 0.1,0.2],[0.2, 0.1,0.3],[0.45, 0.1,0.1]],
    evidence_card = [3],
    evidence=['Autenticacao'],
    state_names={"Biometria": ["Iris", "DigitalAF", "DigitalSAF", "FacialAF", "FacialSAF"], 'Autenticacao':["Forte", "Medio", "Fraco"]}
    )
# print(biometria_cpd)

propriedade_cpd = TabularCPD(
    variable = 'Propriedade',
    variable_card = 4,
    values=[[0.25, 0.25, 0.25], [0.25, 0.25,0.25],[0.25, 0.25,0.25],[0.25, 0.25,0.25]],
    evidence_card = [3],
    evidence=['Autenticacao'],
    state_names={"Propriedade": ["CelularCA", "CelularSCA", "HardKey", "Cartao"], 'Autenticacao':["Forte", "Medio", "Fraco"]}
    )
# print(propriedade_cpd)

#endregion

modelo_seguranca.add_cpds(autenticacao_cpd, tupla_cpd,
                      atualizacao_cpd, case_sensitive_cpd,
                      alfanumerico_cpd, minimo_caracteres_cpd,
                      caractere_especial_cpd, biometria_cpd,
                      propriedade_cpd)

# atualizacao_dist = inferencia.query(['Atualizacao'])
# print(atualizacao_dist)

# case_sensitive_dist = inferencia.query(['CaseSensitive'])
# print(case_sensitive_dist)

# alfanumerico_dist = inferencia.query(['Alfanumerico'])
# print(alfanumerico_dist)

# minimo_caracteres_dist = inferencia.query(['MinimoCaracteres'])
# print(minimo_caracteres_dist)

# caractere_especial_dist = inferencia.query(['CaractereEspecial'])
# print(caractere_especial_dist)

# tupla_dist = inferencia.query(['Tupla'])
# print(tupla_dist)


# biometria_dist = inferencia.query(['Biometria'])
# print(biometria_dist)


# propriedade_dist = inferencia.query(['Propriedade'])
# print(propriedade_dist)

# autenticacao_dist = inferencia.query(['Autenticacao'])
# print(autenticacao_dist)

def gerar_inferencia(query):
    inferencia = VariableElimination(modelo_seguranca)
    return inferencia.query(query[0], evidence=query[1])

# inferencia = VariableElimination(modelo_seguranca)
# autenticacao_dist = inferencia.query(['Autenticacao'], evidence={'Tupla' : 'Forte', 'Biometria' : 'Iris', 'Propriedade': 'CelularCA'})
