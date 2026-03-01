import plotly.express as px

dados = {
    "Aluno": ["João", "Ana", "Maria", "Pedro", "Jorge"],
    "Idade": [15, 11, 17, 8, 12]
}
fig = px.bar(dados, x="Aluno", y="Idade", title="idade dos alunos da escola")
fig.show()