#!/bin/bash

echo "🚀 Iniciando ambiente Spark + Jupyter para Análise do Campeonato Brasileiro 2025"
echo "=================================================================="

# Criar diretórios necessários
mkdir -p data
mkdir -p notebooks

echo "📁 Diretórios criados"

# Iniciar containers (reconstruir se necessário)
echo "🐳 Iniciando containers Docker..."
docker-compose up --build -d

echo "⏳ Aguardando containers iniciarem..."
sleep 10

echo "✅ Ambiente pronto!"
echo ""
echo "🌐 Acesse o Jupyter Notebook em: http://localhost:8888"
echo "📊 Acesse o Spark UI em: http://localhost:4040 (após executar o notebook)"
echo ""
echo "📝 Para executar a análise:"
echo "   1. Abra http://localhost:8888"
echo "   2. Navegue até work/"
echo "   3. Abra o notebook: Analise_Campeonato_Brasileiro_2025_Final.ipynb"
echo "   4. Execute todas as células (Cell > Run All)"
echo ""
echo "🛑 Para parar o ambiente: docker-compose down"
