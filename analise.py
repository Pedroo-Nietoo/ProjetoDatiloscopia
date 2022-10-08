import pandas as pd
import plotly.express as px

df = pd.read_csv("/content/drive/MyDrive/Teste/PlanilhaOFC.csv", encoding="ISO-8859-1")
display(df)

display(df.info())
print()
display(df.describe())
print()
display(df.count())

qtde_categoria = df["PACIENTE"].value_counts()
display(qtde_categoria)
print()
qtde_categoria_perc = df["PACIENTE"].value_counts(normalize=True).round(2)
display(qtde_categoria_perc)

# Mão direita - Transtorno mental
tmDP = px.bar(df, x = "POLEGAR D", y = "TRANSTORNO MENTAL", barmode = 'group', color = "PACIENTE") #text_auto=True
tmDP.show()

tmDI = px.bar(df, x = "INDICADOR D", y = "TRANSTORNO MENTAL", barmode = 'group', color = "PACIENTE")
tmDI.show()

tmDME = px.bar(df, x = "MEDIO D", y = "TRANSTORNO MENTAL", barmode = 'group', color = "PACIENTE")
tmDME.show()

tmDA = px.bar(df, x = "ANELAR D", y = "TRANSTORNO MENTAL", barmode = 'group', color = "PACIENTE")
tmDA.show()

tmDMI = px.bar(df, x = "MINIMO D", y = "TRANSTORNO MENTAL", barmode = 'group', color = "PACIENTE")
tmDMI.show()

# Mão esquerda - Transtorno mental
tmDP2 = px.bar(df, x = "POLEGAR E", y = "TRANSTORNO MENTAL", barmode = 'group', color = "PACIENTE")
tmDP2.show()

tmDI2 = px.bar(df, x = "INDICADOR E", y = "TRANSTORNO MENTAL", barmode = 'group', color = "PACIENTE")
tmDI2.show()

tmDME2 = px.bar(df, x = "MEDIO E", y = "TRANSTORNO MENTAL", barmode = 'group', color = "PACIENTE")
tmDME2.show()

tmDA2 = px.bar(df, x = "ANELAR E", y = "TRANSTORNO MENTAL", barmode = 'group', color = "PACIENTE")
tmDA2.show()

tmDMI2 = px.bar(df, x = "MINIMO E", y = "TRANSTORNO MENTAL", barmode = 'group', color = "PACIENTE")
tmDMI2.show()
