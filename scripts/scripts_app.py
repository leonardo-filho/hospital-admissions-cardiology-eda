import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import os

st.set_page_config(layout='wide')
st.title("🏥 Dashboard de Previsão de Mortalidade Hospitalar")

# Carregamento dos dados
@st.cache_data
def load_data():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    admission_path = os.path.join(base_path, "data", "HDHI Admission data.csv")
    mortality_path = os.path.join(base_path, "data", "HDHI Mortality Data.csv")
    
    admission_data = pd.read_csv(admission_path)
    mortality_data = pd.read_csv(mortality_path)
    return admission_data, mortality_data

admissions, mortality = load_data()

# Preprocessamento
admissions['MORTALITY'] = admissions['MRD No.'].isin(mortality['MRD']).astype(int)

# Filtros
st.sidebar.title("🔎 Filtros")
idade_min = int(admissions['AGE'].min())
idade_max = int(admissions['AGE'].max())
idade_range = st.sidebar.slider("Filtrar por idade", idade_min, idade_max, (idade_min, idade_max))
genero = st.sidebar.multiselect("Gênero", options=admissions['GENDER'].unique(), default=admissions['GENDER'].unique())

df_filtered = admissions[(admissions['AGE'] >= idade_range[0]) & 
                         (admissions['AGE'] <= idade_range[1]) & 
                         (admissions['GENDER'].isin(genero))]

# Gráfico de mortalidade
st.subheader("Distribuição da Mortalidade")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    sns.countplot(x='MORTALITY', hue='GENDER', data=df_filtered, ax=ax)
    ax.set_xticklabels(['Vivo', 'Óbito'])
    ax.set_title("Mortalidade por Gênero")
    ax.set_ylabel("Número de Pacientes")
    ax.set_xlabel("Desfecho")
    ax.legend(title='Gênero')
    st.pyplot(fig)

with col2:
    tabela = df_filtered[['AGE', 'GENDER', 'MORTALITY']].groupby(['GENDER', 'MORTALITY']).size().unstack().fillna(0)
    tabela.columns = ['Vivo', 'Óbito']
    st.write(tabela)

# Modelo
st.subheader("🎯 Previsão com Random Forest")

features = admissions.select_dtypes(include=['int64', 'float64']).drop(columns=['SNO'])
X = features.drop(columns=['MORTALITY'])
y = features['MORTALITY']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

st.markdown("**Métricas do Modelo:**")
st.write("Acurácia:", round(accuracy_score(y_test, y_pred), 3))
st.text("Relatório de Classificação:")
st.text(classification_report(y_test, y_pred))

# Exibir a tabela completa
st.subheader("📋 Tabela de Admissões Filtradas")
st.dataframe(df_filtered)
