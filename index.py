import requests
r = requests.get('https://api.exchangeratesapi.io/latest?base=GBP&symbols=IDR')
kurs=r.json()
# Using readlines() 

file1 = open('resa.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines: 
    if "#" not in line:
        # print(line)
        count+=1
    # else:
        # print(line)
kurs=kurs["rates"]["IDR"]
jumlah=kurs*count
popo="""
**JUMLAH LINK YANG DI SCRAPE RESA** : %s
**KURS GBP/IDR SAAT INI**: %s
KURS DIDAPATKAN DARI https://api.exchangeratesapi.io/latest?base=GBP&symbols=IDR
**JUMLAH YANG HARUS DIBAYARKAN KE QULYUBI SETELAH WITHDRAW 

# 💰 %s RUPIAH
""" % (str(count),str(kurs),str(jumlah))
f = open("README.md", "w")
f.write(popo)
f.close()