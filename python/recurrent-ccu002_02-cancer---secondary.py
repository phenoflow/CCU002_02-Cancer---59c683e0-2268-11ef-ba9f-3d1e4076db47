# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"314976006","system":"icd10"},{"code":"314952003","system":"icd10"},{"code":"71111000119109","system":"icd10"},{"code":"314954002","system":"icd10"},{"code":"314963000","system":"icd10"},{"code":"1098981000119101","system":"icd10"},{"code":"314951005","system":"icd10"},{"code":"314973003","system":"icd10"},{"code":"314966008","system":"icd10"},{"code":"314962005","system":"icd10"},{"code":"314960002","system":"icd10"},{"code":"314965007","system":"icd10"},{"code":"314961003","system":"icd10"},{"code":"1081561000119108","system":"icd10"},{"code":"1081551000119106","system":"icd10"},{"code":"314955001","system":"icd10"},{"code":"314969001","system":"icd10"},{"code":"314967004","system":"icd10"},{"code":"314974009","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["recurrent-ccu002_02-cancer---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["recurrent-ccu002_02-cancer---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["recurrent-ccu002_02-cancer---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
