FROM jupyter/pyspark-notebook:spark-3.4.1

# Instalar dependências adicionais como root
USER root

# Instalar dependências do sistema se necessário
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Voltar para usuário jovyan
USER jovyan

# Copiar requirements.txt
COPY requirements.txt /tmp/requirements.txt

# Instalar dependências Python
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Configurar diretório de trabalho
WORKDIR /home/jovyan
