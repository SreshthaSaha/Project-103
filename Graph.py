import pandas as pd
import plotly_express as px

df = pd.read_csv("data.csv")
graph = px.scatter(df,x="date",y="cases",color="country",size_max=30,title="Covid cases in different countries")
graph.show()