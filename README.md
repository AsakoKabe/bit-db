# bit-db

DragonflyDB - CP
Then comes the case of Network Partition (P), and if (P) happens then Redis becomes unvailable in the minority partition. That's why from CAP perspective, Redis is CP because it becomes unavailable in minority partitions. Please note it will still be available in majority partition.
источники:
https://stackoverflow.com/questions/59511275/redis-availability-and-cap-theorem
https://www.dragonflydb.io/guides/cache-database
https://www.dragonflydb.io/faq/key-value-database-vs-cassandra

ScyllaDB - AP
The CAP Theorem is the notion that C (Consistency), A (Availability) and P (Partition Tolerance) of data are mutually dependent in a distributed system. Increasing any 2 of these factors will reduce the third. Scylla chooses availability and partition tolerance over consistency
источники:
https://opensource.docs.scylladb.com/stable/reference/glossary.html

ArenadataDB - CP
The system is fully ACID-compliant, i.e. the same tables can be used for reading and writing, with no risk of data loss.
источники:
https://arenadata.tech/en/products/arenadata-db/