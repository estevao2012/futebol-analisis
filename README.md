# ⚽ Análise do Campeonato Brasileiro 2025 com Apache Spark

Trabalho Final - Big Data Analytics usando Apache Spark, Spark SQL e Spark MLlib.

## 🚀 Início Rápido

### Opção 1: Ambiente Local (Recomendado)
```bash
# 1. Criar ambiente virtual
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Iniciar Jupyter
./start-local.sh
```

### Opção 2: Docker
```bash
# 1. Iniciar containers
./start.sh

# 2. Acessar Jupyter
# http://localhost:8888
```

### 3. Executar Análise
- Abra: `Analise_Campeonato_Brasileiro_2025_Final.ipynb`
- Execute todas as células: `Cell > Run All`
- Monitorar Spark UI: http://localhost:4040

## 📊 O que o notebook faz

1. **Configura Apache Spark** em modo local
2. **Gera dados sintéticos** do Campeonato Brasileiro 2025:
   - 20 times
   - 38 rodadas (380 partidas)
   - 38.000 eventos de futebol
   - 220 jogadores

3. **Análises com Spark SQL**:
   - Top times por gols, passes, faltas
   - Estatísticas por rodada
   - Artilheiros do campeonato

4. **Machine Learning com Spark MLlib**:
   - Clustering de times (5 grupos)
   - Clustering de jogadores (5 grupos)
   - Pipeline completo com normalização

5. **Visualizações**:
   - Gráficos dos top times
   - Distribuição de eventos

## 🛠️ Tecnologias

- **Apache Spark 3.4** (modo local)
- **Spark SQL** para análises
- **Spark MLlib** para clustering
- **Jupyter Notebook** para interface
- **Docker** para ambiente isolado

## 📁 Estrutura

```
├── docker-compose.yml          # Configuração Docker
├── start.sh                    # Script de inicialização
├── Analise_Campeonato_Brasileiro_2025_Final.ipynb  # Notebook principal
├── data/                       # Dados gerados
└── notebooks/                  # Notebooks adicionais
```

## 🛑 Parar o ambiente

```bash
docker-compose down
```

## 📋 Requisitos Atendidos

- ✅ Análise de eventos esportivos
- ✅ Apache Spark para processamento
- ✅ Spark SQL para consultas
- ✅ Spark MLlib para Machine Learning
- ✅ Clustering K-Means
- ✅ Visualizações e gráficos
- ✅ Jupyter Notebook executável
- ✅ Massa de dados significativa (38k eventos)

## 🎯 Resultados Esperados

O notebook irá:
1. Processar 38.000 eventos em tempo real
2. Identificar 5 perfis de times via clustering
3. Classificar 220 jogadores em 5 grupos
4. Gerar estatísticas completas do campeonato
5. Criar visualizações dos resultados
