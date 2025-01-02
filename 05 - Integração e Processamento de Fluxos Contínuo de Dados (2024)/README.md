# Acessar máquina kafka
docker exec -it kafka bash 

# Acessar diretório kafka
cd opt/kafka/bin 

# Criar tópico
./kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic aula

# Deletar tópico
./kafka-topics.sh --zookeeper zookeeper:2181 --delete --topic aula

# Listar tópicos
./kafka-topics.sh --list --zookeeper zookeeper:2181

# Descrever tópicos
./kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic aula
./kafka-topics.sh --describe --zookeeper zookeeper:2181

# Escrever uma mensagem no tópico
./kafka-console-producer.sh --broker-list kafka:9092 --topic aula
teste
teste1
aula de ingestao de dados
outras mensagens

# Os logs do kafka
    Ficam em: cd kafka/kafka-logs-kafka/

# Startar um consumer:
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic aula

# Startar um consumer do inicio das mensagens:
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic aula --from-beginning

# Acessar jupyter notebooks:
localhost:8089
