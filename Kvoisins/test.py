import KvoisinsSimple as Kv
import csv

Filename = "iris"
with open("./Kvoisins/"+Filename+".csv", 'r', encoding="utf-8", newline='') as file:
    dbR = csv.reader(file, delimiter=",")
    FileData = [i for i in dbR][1:]
#print(FileData)
ano = [4.1,1.0,5.9,2.1]

retval = Kv.KVoisins(ano, FileData, typeindex=4, K=5)
(iD, prob) = retval
print(f"type de donnée : {iD}")
print(f"Probabilité : {prob}%")