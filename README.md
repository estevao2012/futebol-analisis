# Análise de Eventos de Futebol (execução via Docker)

Para executar este projeto, utilize Docker.

1. Execute a imagem oficial Jupyter com Spark:

```bash
docker run -it --rm \
  -p 8888:8888 -p 4040:4040 \
  -v "$(pwd)":/home/jovyan/work \
  jupyter/pyspark-notebook:latest
```

2. Acesse o Jupyter na porta 8888 informada no terminal.

3. Abra o notebook em:
- work/Analise_Campeonato_Brasileiro_2025_Final.ipynb

4. Execute todas as células na ordem indicada no notebook:
- Setup
- Geração de dados
- Publicação (file sink)
- Leitura (structured streaming com trigger once)
- Análises, ML e gráficos
- Encerrar Spark

5. Spark UI disponível em http://localhost:4040 (durante a sessão Spark).

Observações:
- Os diretórios data/stream_inbox e data/stream_ckpt são gerados em tempo de execução e estão ignorados no versionamento.
- O processamento ocorre sequencialmente sem esperas artificiais.
