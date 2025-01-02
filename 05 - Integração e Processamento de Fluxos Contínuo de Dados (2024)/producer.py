from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

topic = 'aula'
mensagem = b'Sua mensagem para o Kafka!'

producer.send(topic, mensagem)
