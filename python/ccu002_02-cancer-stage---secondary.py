# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"956431000000100","system":"icd10"},{"code":"956391000000108","system":"icd10"},{"code":"956551000000106","system":"icd10"},{"code":"956411000000108","system":"icd10"},{"code":"956371000000109","system":"icd10"},{"code":"956471000000103","system":"icd10"},{"code":"956451000000107","system":"icd10"},{"code":"956511000000107","system":"icd10"},{"code":"956351000000100","system":"icd10"},{"code":"956531000000104","system":"icd10"},{"code":"956331000000107","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-stage---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-stage---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-stage---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
