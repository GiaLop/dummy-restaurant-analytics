"""
Utility functions per analisi Food Cost ristoranti
Autore: Giovanni Lo Presti
Data: Ottobre 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display


def eda_display(df):
  """
  Automatizzo la visualizzazione delle stats di un dataset

  Args:
      df = dataframe caricato in precedenza

  Return:
      df:
      - head()
      - info()
      - describe()
      - somma NaN values
      - df con % NaN per Serie
      - duplicated()

  Requirements:
  pandas
  """

  print('DATASET HEAD:')
  display(df.head(15))

  print('-' * 70)
  print('-' * 70)
  print('INFO:')
  display(df.info())

  print('-' * 70)
  print('-' * 70)
  print('DESCRIBE:')
  display(df.describe())

  print('-' * 70)
  print('-' * 70)
  print('NAN VALUES:')
  display(df.isna().sum())
  missing = df.isna().sum()
  missing_pct = (df.isna().sum() / len(df) * 100).round(2)
  missing_df = pd.DataFrame({
        'Missing Count': missing,
        'Percentage': missing_pct
    })
  display(missing_df[missing_df['Missing Count'] > 0])

  print('-' * 70)
  print('-' * 70)
  print('DUPLICATED:')
  print(df.duplicated().sum())


def risparmio_foodcost(ds, nome_piatto, fc_target):

  """
  Calcola il risparmio potenziale inserendo il food cost ottimale

  Args:
      nome_piatto (str): Nome del piatto da analizzare
      fc_target (float): Food cost % ottimale da rasggiungere

  Return:
      Dict con tutti i calcoli eseguiti
  """

  # cerco il piatto nel df per accedere ai dati del piatto
  piatto = ds[ds['dish_name'] == nome_piatto]

  #verifico che il piatto esista
  if piatto.empty:
    return f"{nome_piatto} non trovato!"

  # trovo dati di riferimento sul piatto
  prezzo_piatto = piatto['selling_price'].iloc[0]
  costo_piatto = piatto['unit_cost'].iloc[0]
  spreco_piatto = piatto['waste_qty'].iloc[0]
  unit_piatto_vendute = piatto['quantity_sold'].sum()

  # calcolo food cost attuale
  fc_attuale = ((costo_piatto + spreco_piatto) / prezzo_piatto) * 100

  # calcolo il costo target per soddisfare il fc% di riferimento
  costo_target = (fc_target * prezzo_piatto) / 100

  # calcolo il risparmio potenziale
  risparmio = costo_piatto - costo_target
  risparmio_potenziale = risparmio * unit_piatto_vendute

  # aggiungo la colonna category
  categoria = piatto['category'].iloc[0]

  return {
      'nome piatto' : nome_piatto,
      'categoria' : categoria,
      'prezzo piatto' : round(float(prezzo_piatto),2),
      'costo piatto' : round(float(costo_piatto),2),
      'costo target' : round(float(costo_target),2),
      'unità vendute' : int(unit_piatto_vendute),
      'food cost % attuale' : round(float(fc_attuale),2),
      'food cost % target' : round(float(fc_target),2),
      'costo target' : round(float(costo_target),2),
      'risparmio per unità' : round(float(risparmio),2),
      'risparmio potenziale': round(float(risparmio_potenziale),2)
  }



