import pandas as pd
import joblib





scaler = joblib.load('database/scaler.pkl')
modelo_carregado = joblib.load("database/modelo_evasao.pkl")