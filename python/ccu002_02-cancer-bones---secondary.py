# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"271467005","system":"icd10"},{"code":"134421000","system":"icd10"},{"code":"712849003","system":"icd10"},{"code":"285618001","system":"icd10"},{"code":"314990009","system":"icd10"},{"code":"428281000","system":"icd10"},{"code":"187903000","system":"icd10"},{"code":"372108006","system":"icd10"},{"code":"449627008","system":"icd10"},{"code":"307576001","system":"icd10"},{"code":"93916003","system":"icd10"},{"code":"269467007","system":"icd10"},{"code":"93725000","system":"icd10"},{"code":"712525007","system":"icd10"},{"code":"94145009","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-bones---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-bones---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-bones---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
