import json
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

autenticacao_cpd = TabularCPD(
    variable = 'Autenticacao',
    variable_card = 3,
    values=[[0.2], [0.3],[0.5]],
    state_names={"Autenticacao": ["Forte", "Medio", "Fraco"]}
)

tupla_cpd = TabularCPD(
    variable='Tupla',
    variable_card=3,
    values=[[0.4, 0.2, 0.1], [0.3, 0.3, 0.4], [0.3, 0.5, 0.5]],
    evidence_card=[3],
    evidence=['Autenticacao'],
    state_names={"Tupla": ["Forte", "Medio", "Fraco"], 'Autenticacao':["Forte", "Medio", "Fraco"]}
    )

atualizacao_cpd = TabularCPD(
    variable = 'Atualizacao',
    variable_card = 2,
    values=[[0.9, 0.7, 0.5], [0.1, 0.3,0.5]],
    evidence_card = [3],
    evidence=['Tupla'],
    state_names={"Atualizacao": ["Sim", "Nao"], 'Tupla':["Forte", "Medio", "Fraco"]}
    )

case_sensitive_cpd = TabularCPD(
    variable = 'CaseSensitive',
    variable_card = 2,
    values=[[0.9, 0.7, 0.5], [0.1, 0.3,0.5]],
    evidence_card = [3],
    evidence=['Tupla'],
    state_names={"CaseSensitive": ["Sim", "Nao"], 'Tupla':["Forte", "Medio", "Fraco"]}
    )

alfanumerico_cpd = TabularCPD(
    variable = 'Alfanumerico',
    variable_card = 2,
    values=[[0.9, 0.7, 0.5], [0.1, 0.3,0.5]],
    evidence_card = [3],
    evidence=['Tupla'],
    state_names={"Alfanumerico": ["Sim", "Nao"], 'Tupla':["Forte", "Medio", "Fraco"]}
    )

minimo_caracteres_cpd = TabularCPD(
    variable = 'MinimoCaracteres',
    variable_card = 2,
    values=[[0.9, 0.7, 0.5], [0.1, 0.3,0.5]],
    evidence_card = [3],
    evidence=['Tupla'],
    state_names={"MinimoCaracteres": ["Sim", "Nao"], 'Tupla':["Forte", "Medio", "Fraco"]}
    )

caractere_especial_cpd = TabularCPD(
    variable = 'CaractereEspecial',
    variable_card = 2,
    values=[[0.9, 0.7, 0.5], [0.1, 0.3,0.5]],
    evidence_card = [3],
    evidence=['Tupla'],
    state_names={"CaractereEspecial": ["Sim", "Nao"], 'Tupla':["Forte", "Medio", "Fraco"]}
    )

biometria_cpd = TabularCPD(
    variable = 'Biometria',
    variable_card = 5,
    values=[[0.02, 0.005, 0.001], [0.1, 0.08,0.06],[0.7, 0.75,0.8],[0.05, 0.04,0.03],[0.13, 0.125,0.109]],
    evidence_card = [3],
    evidence=['Autenticacao'],
    state_names={"Biometria": ["Iris", "DigitalAF", "DigitalSAF", "FacialAF", "FacialSAF"], 'Autenticacao':["Forte", "Medio", "Fraco"]}
    )

propriedade_cpd = TabularCPD(
    variable = 'Propriedade',
    variable_card = 4,
    values=[[0.50, 0.40, 0.35], [0.25, 0.30,0.55],[0.15, 0.10,0.05],[0.10, 0.20,0.05]],
    evidence_card = [3],
    evidence=['Autenticacao'],
    state_names={"Propriedade": ["CelularCA", "CelularSCA", "HardKey", "Cartao"], 'Autenticacao':["Forte", "Medio", "Fraco"]}
    )

modelo_seguranca.add_cpds(autenticacao_cpd, tupla_cpd,
                      atualizacao_cpd, case_sensitive_cpd,
                      alfanumerico_cpd, minimo_caracteres_cpd,
                      caractere_especial_cpd, biometria_cpd,
                      propriedade_cpd)

def gerar_inferencia(query):
    inferencia = VariableElimination(modelo_seguranca)
    autenticacao_dist = inferencia.query(query[0], evidence=query[1])
    json_response = {
        "Autenticacao(Forte)": autenticacao_dist.values[0],
        "Autenticacao(Medio)": autenticacao_dist.values[1],
        "Autenticacao(Fraco)": autenticacao_dist.values[2],
    }

    return json.dumps(json_response)

# inferencia = VariableElimination(modelo_seguranca)
# autenticacao_dist = inferencia.query(['Autenticacao'], evidence={'CaractereEspecial': 'Sim', 'MinimoCaracteres': 'Sim', 'Biometria' : 'DigitalSAF', 'Propriedade': 'CelularSCA'})
