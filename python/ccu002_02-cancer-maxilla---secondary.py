# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"363502009","system":"icd10"},{"code":"188537004","system":"icd10"},{"code":"188568000","system":"icd10"},{"code":"188578002","system":"icd10"},{"code":"188641006","system":"icd10"},{"code":"188492005","system":"icd10"},{"code":"188049009","system":"icd10"},{"code":"363425008","system":"icd10"},{"code":"188513004","system":"icd10"},{"code":"93194002","system":"icd10"},{"code":"188612002","system":"icd10"},{"code":"93541001","system":"icd10"},{"code":"269616004","system":"icd10"},{"code":"94710006","system":"icd10"},{"code":"94180008","system":"icd10"},{"code":"188010006","system":"icd10"},{"code":"93888008","system":"icd10"},{"code":"188665009","system":"icd10"},{"code":"93889000","system":"icd10"},{"code":"449077005","system":"icd10"},{"code":"188589009","system":"icd10"},{"code":"188503007","system":"icd10"},{"code":"93523009","system":"icd10"},{"code":"188547001","system":"icd10"},{"code":"188558005","system":"icd10"},{"code":"188633006","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-maxilla---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-maxilla---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-maxilla---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
