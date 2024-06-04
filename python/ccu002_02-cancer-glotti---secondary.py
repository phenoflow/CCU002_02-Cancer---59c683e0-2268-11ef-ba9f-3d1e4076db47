# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"254517003","system":"icd10"},{"code":"363430007","system":"icd10"},{"code":"187842004","system":"icd10"},{"code":"187708004","system":"icd10"},{"code":"93784003","system":"icd10"},{"code":"363487003","system":"icd10"},{"code":"187682009","system":"icd10"},{"code":"254520006","system":"icd10"},{"code":"187683004","system":"icd10"},{"code":"187841006","system":"icd10"},{"code":"187681002","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-glotti---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-glotti---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-glotti---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
