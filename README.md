# Análise de Eventos de Futebol (execução via Docker)

Execute este projeto usando Docker Compose.

## 1) Criar docker-compose.yml na raiz do projeto

```yaml
version: '3.8'
services:
  jupyter:
    image: jupyter/pyspark-notebook:latest
    container_name: football_jupyter
    environment:
      - JUPYTER_ENABLE_LAB=yes
      - GRANT_SUDO=yes
    ports:
      - "8888:8888"
      - "4040:4040"  # Spark UI
    volumes:
      - .:/home/jovyan/work
    working_dir: /home/jovyan
    command: start-notebook.sh --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_root=True
```

## 2) Subir o ambiente

```bash
docker-compose up -d
```

## 3) URLs de acesso
- Jupyter: http://localhost:8888
- Spark UI: http://localhost:4040

## 4) Abrir o notebook
- Caminho no Jupyter: work/Analise_Campeonato_Brasileiro_2025_Final.ipynb

## 5) Executar as células (nesta ordem)
- Run > Restart Kernel And Run All Cells

## 6) Encerrar o ambiente
```bash
docker-compose down
```
