#!/usr/bin/env python3
"""
Script para configurar variáveis de ambiente para PySpark no VSCode
"""
import os
import sys
import subprocess

def setup_java_env():
    """Configura as variáveis de ambiente do Java para PySpark"""
    
    # Possíveis localizações do Java
    java_paths = [
        "/opt/homebrew/opt/openjdk@11",
        "/opt/homebrew/opt/openjdk@8", 
        "/usr/libexec/java_home",
        "/Library/Java/JavaVirtualMachines"
    ]
    
    java_home = None
    
    # Tentar encontrar Java via java_home
    try:
        result = subprocess.run(["/usr/libexec/java_home", "-v", "11"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            java_home = result.stdout.strip()
            print(f"✅ Java encontrado via java_home: {java_home}")
    except:
        pass
    
    # Se não encontrou, tentar Homebrew
    if not java_home:
        for path in java_paths:
            if os.path.exists(path) and "homebrew" in path:
                java_home = path
                print(f"✅ Java encontrado no Homebrew: {java_home}")
                break
    
    if java_home:
        # Configurar variáveis de ambiente
        os.environ["JAVA_HOME"] = java_home
        os.environ["PATH"] = f"{java_home}/bin:{os.environ.get('PATH', '')}"
        
        # Para PySpark
        os.environ["PYSPARK_SUBMIT_ARGS"] = "--master local[*] pyspark-shell"
        
        print(f"🔧 JAVA_HOME configurado: {java_home}")
        print(f"🔧 PATH atualizado")
        
        return True
    else:
        print("❌ Java não encontrado!")
        print("Instale o Java com: brew install openjdk@11")
        return False

def test_spark():
    """Testa se o Spark está funcionando"""
    try:
        import findspark
        findspark.init()
        
        from pyspark.sql import SparkSession
        
        spark = SparkSession.builder \
            .appName("TestSpark") \
            .master("local[*]") \
            .config("spark.sql.adaptive.enabled", "true") \
            .getOrCreate()
        
        # Teste simples
        df = spark.createDataFrame([(1, "test")], ["id", "name"])
        count = df.count()
        
        spark.stop()
        
        print(f"✅ Spark funcionando! Teste executado com sucesso (count: {count})")
        return True
        
    except Exception as e:
        print(f"❌ Erro no Spark: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Configurando ambiente PySpark...")
    
    if setup_java_env():
        print("☕ Java configurado com sucesso!")
        
        if test_spark():
            print("⚡ Spark testado com sucesso!")
            print("\n✅ Ambiente pronto para usar!")
        else:
            print("\n❌ Problema com Spark")
    else:
        print("\n❌ Problema com Java")
