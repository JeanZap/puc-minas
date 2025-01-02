from kafka import KafkaConsumer

consumer = KafkaConsumer('aula', group_id='python-local',
                         bootstrap_servers='localhost:9092')

for message in consumer:
    print(message.topic)
    print(message.offset)
    print(message.value)
    print('------------')
