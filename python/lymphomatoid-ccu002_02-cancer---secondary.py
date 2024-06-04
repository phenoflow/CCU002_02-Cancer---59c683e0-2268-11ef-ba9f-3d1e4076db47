# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"276811008","system":"icd10"},{"code":"736322001","system":"icd10"},{"code":"276836002","system":"icd10"},{"code":"93198004","system":"icd10"},{"code":"847741000000106","system":"icd10"},{"code":"109988003","system":"icd10"},{"code":"847481000000109","system":"icd10"},{"code":"277641001","system":"icd10"},{"code":"308121000","system":"icd10"},{"code":"429014004","system":"icd10"},{"code":"109979007","system":"icd10"},{"code":"109962001","system":"icd10"},{"code":"277654008","system":"icd10"},{"code":"277615007","system":"icd10"},{"code":"95193005","system":"icd10"},{"code":"307636001","system":"icd10"},{"code":"118600007","system":"icd10"},{"code":"269476000","system":"icd10"},{"code":"118617000","system":"icd10"},{"code":"118601006","system":"icd10"},{"code":"188516007","system":"icd10"},{"code":"1091921000000103","system":"icd10"},{"code":"847651000000100","system":"icd10"},{"code":"847631000000107","system":"icd10"},{"code":"302841002","system":"icd10"},{"code":"445406001","system":"icd10"},{"code":"276815004","system":"icd10"},{"code":"109977009","system":"icd10"},{"code":"232075002","system":"icd10"},{"code":"277664004","system":"icd10"},{"code":"847691000000108","system":"icd10"},{"code":"277616008","system":"icd10"},{"code":"763477007","system":"icd10"},{"code":"278052009","system":"icd10"},{"code":"277642008","system":"icd10"},{"code":"277570003","system":"icd10"},{"code":"762690000","system":"icd10"},{"code":"109965004","system":"icd10"},{"code":"277623009","system":"icd10"},{"code":"277551008","system":"icd10"},{"code":"236513009","system":"icd10"},{"code":"109975001","system":"icd10"},{"code":"31047003","system":"icd10"},{"code":"420788006","system":"icd10"},{"code":"277618009","system":"icd10"},{"code":"847701000000108","system":"icd10"},{"code":"109978004","system":"icd10"},{"code":"240531002","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lymphomatoid-ccu002_02-cancer---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lymphomatoid-ccu002_02-cancer---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lymphomatoid-ccu002_02-cancer---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
