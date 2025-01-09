import conection
import boto3
import requests
import os


def get_consultas():
    connection = conection.get_connection()
    cursor = connection.cursor()
    cursor.execute("select CAMINHO_ARQUIVO from TBL_FATURA_ENERGIA tfe where NUM_NF = '107687488'")
    consultas = [consulta[0] for consulta in cursor.fetchall()]
    print("Resultados encontrados:")
    for consulta in consultas:
        print(consulta)
    return consultas

def get_download_file(consultas):
    # Itera sobre cada URL na lista de consultas
    for consulta in consultas:
        try:
            # Remove os colchetes e aspas se existirem
            url = consulta.strip('[]\'\"')
            print(f"Tentando baixar arquivo de: {url}")
            response = requests.get(url)
            response.raise_for_status()
            
            # Extrai o nome do arquivo da URL
            filename = url.split('/')[-1]
            
            # Salva o arquivo localmente
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Arquivo {filename} baixado com sucesso!")
            
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar arquivo: {e}")
    
def main():
    connection = conection.get_connection()
    print("Conexao realizada com sucesso")
    
    # Obtém a lista de URLs
    consultas = get_consultas()
    
    # Passa a lista para a função de download
    get_download_file(consultas)

if __name__ == "__main__":
    main()  


