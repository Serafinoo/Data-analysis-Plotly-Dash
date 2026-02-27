import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
dados = pd.DataFrame({
    "Frequência": ["Semanalmente", "Mensalmente", "Semestralmente", "Anualmente", "Nenhum", "Total"],
    "FA": [4, 12, 1, 1, 1, 18],
    "FR": [0.22, 0.66, 0.055, 0.055, 0.055, 1.0]
})

comidas = pd.DataFrame({
    "Exemplares": ["Açaí", "Maniçoba", "Tacacá", "Vatapá", "Mariscada", "Caruru", "Arroz Paraense", "Nenhum", "Total"],
    "FA": [13, 3, 0, 2, 0, 0, 0, 1, 18],
    "FR": [0.715, 0.165, 0, 0.11, 0, 0, 0, 0.055, 1.0]
})

fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "bar"}, {"type": "pie"}]],
    subplot_titles=("Frequência de consumo comidas típicas: 2º EM - Vespertino", "Comidas típicas favoritas: 2º EM - Vespertino")
)

fig.add_trace(
    go.Bar(
        x=dados["Frequência"],
        y=dados["FR"]
        text=dados["FA"]
        textposition="outside"
        fig.update_yaxes(tickformat=".0%", row=1, col=1)
    ),
    row=1, col=1
)

fig.add_trace(
    go.Pie(
        labels=comidas["Exemplares"],
        values=comidas["FA"]
    ),
    row=1,col=2
)

fig.update_layout(title="Comidas Típicas: 2º EM - Vespertino")
fig.show()

#    fig = px.bar(dados, x="Frequência", y="FR", text="FA", title="Frequência de consumo comidas típicas: 2º EM - Vespertino")
#    fig.update_layout(yaxis_tickformat=".0%")
#    fig.update_traces(textposition="outside")
#    fig.show()
#
#    fig2 = px.pie(comidas, names="Exemplares", values="FA",title="Comidas típicas favoritas: 2º EM - Vespertino")
#    fig2.update_layout(yaxis_tickformat=".0%")
#    fig2.show()