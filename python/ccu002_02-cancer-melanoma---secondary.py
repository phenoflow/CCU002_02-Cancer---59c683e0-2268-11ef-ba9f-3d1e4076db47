# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"C43","system":"icd10"},{"code":"188075008","system":"icd10"},{"code":"372244006","system":"icd10"},{"code":"188063003","system":"icd10"},{"code":"403927001","system":"icd10"},{"code":"188068007","system":"icd10"},{"code":"188033007","system":"icd10"},{"code":"188038003","system":"icd10"},{"code":"188070003","system":"icd10"},{"code":"403924008","system":"icd10"},{"code":"188042000","system":"icd10"},{"code":"402558004","system":"icd10"},{"code":"255012009","system":"icd10"},{"code":"188055004","system":"icd10"},{"code":"188046002","system":"icd10"},{"code":"188040008","system":"icd10"},{"code":"188076009","system":"icd10"},{"code":"302837001","system":"icd10"},{"code":"276821000","system":"icd10"},{"code":"276751004","system":"icd10"},{"code":"93655004","system":"icd10"},{"code":"188073001","system":"icd10"},{"code":"310498001","system":"icd10"},{"code":"93223008","system":"icd10"},{"code":"188074007","system":"icd10"},{"code":"269578002","system":"icd10"},{"code":"93643005","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-melanoma---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-melanoma---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-melanoma---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
