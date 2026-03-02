import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

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
    rows=1, 
    cols=2,
    specs=[[{"type": "bar"}, {"type": "pie"}]],
    subplot_titles=("Frequência de consumo comidas típicas: 2º EM - Vespertino", "Comidas típicas favoritas: 2º EM - Vespertino")
)

fig.add_trace(
    go.Bar(
        x=dados["Frequência"],
        y=dados["FR"],
        text=dados["FA"],
        textposition="outside",
    ),
    row=1, col=1
)

fig.update_yaxes(tickformat=".0%", row=1, col=1)

fig.add_trace(
    go.Pie(
        labels=comidas["Exemplares"],
        values=comidas["FA"]
    ),
    row=1, col=2,
)

fig.update_layout(title="Comidas Típicas: 2º EM - Vespertino")

app.layout = html.Div([
    html.H1("Dashboard de Pesquisa"),
    dcc.Graph(figure=fig)
])

app.layout = html.Div(
    className="dashboard-container",
    children=[
        html.H1("Dashboard de Pesquisa"),

        html.Div(
            className="card",
            children=[
                dcc.Graph(figure=fig)
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)