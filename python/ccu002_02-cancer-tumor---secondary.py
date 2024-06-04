# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"363358000","system":"icd10"},{"code":"277605001","system":"icd10"},{"code":"363396004","system":"icd10"},{"code":"363382005","system":"icd10"},{"code":"363488008","system":"icd10"},{"code":"187752007","system":"icd10"},{"code":"363456000","system":"icd10"},{"code":"255096006","system":"icd10"},{"code":"359987004","system":"icd10"},{"code":"254828009","system":"icd10"},{"code":"363490009","system":"icd10"},{"code":"254638002","system":"icd10"},{"code":"363436001","system":"icd10"},{"code":"253017000","system":"icd10"},{"code":"255056009","system":"icd10"},{"code":"188286001","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-tumor---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-tumor---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-tumor---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
