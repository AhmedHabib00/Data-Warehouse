FROM confluentinc/cp-kafka-connect-base

# Install the JDBC connector
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.0.0
# Install the mongo connector
RUN confluent-hub install --no-prompt mongodb/kafka-connect-mongodb:1.5.0
# Install hdfs connector
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-hdfs:10.0.0
# Install Debezium connector for postgres
RUN confluent-hub install --no-prompt debezium/debezium-connector-postgresql:1.6.0
