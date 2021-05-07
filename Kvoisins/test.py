import KvoisinsSimple as Kv
import csv

Filename = "iris"
with open("./Kvoisins/"+Filename+".csv", 'r', encoding="utf-8", newline='') as file:
    dbR = csv.reader(file, delimiter=",")
    FileData = [i for i in dbR][1:]
#print(FileData)
ano = [5.7,4.4,1.5,0.4,"setosa"]

retval = Kv.KVoisins(ano, FileData, typeindex=4)
(iD, prob) = retval
print(f"type de donnée : {iD}")
print(f"Probabilité : {prob}%")