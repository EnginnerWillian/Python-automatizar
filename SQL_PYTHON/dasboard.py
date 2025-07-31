












import dash
import plotly.express es px
import padnas  as  pd

app = Dash(__name__)

df = pd.Dataframe({
    "Fruit":["Apples", "Oranges", "Bananas", "Apples", "Bananas"],
    "Amount":[4, 1, 2, 2, 4, 5],
    "City":["SP", "SP", "SP", "Mountreal",  "Montreal"]
})
fig = px.bar(df,x="Fruit", y="Amount", colot="City", barmode="group")
app.layout = htal.Div(children=
                      html.H1(childrem="Hello dash"))