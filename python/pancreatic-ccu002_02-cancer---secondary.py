# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"C25","system":"icd10"},{"code":"255088001","system":"icd10"},{"code":"700423003","system":"icd10"},{"code":"735735001","system":"icd10"},{"code":"254611009","system":"icd10"},{"code":"372003004","system":"icd10"},{"code":"187791002","system":"icd10"},{"code":"235966007","system":"icd10"},{"code":"187798008","system":"icd10"},{"code":"285614004","system":"icd10"},{"code":"363418001","system":"icd10"},{"code":"187792009","system":"icd10"},{"code":"187793004","system":"icd10"},{"code":"372119009","system":"icd10"},{"code":"314964006","system":"icd10"},{"code":"363419009","system":"icd10"},{"code":"314999005","system":"icd10"},{"code":"109848009","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pancreatic-ccu002_02-cancer---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pancreatic-ccu002_02-cancer---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pancreatic-ccu002_02-cancer---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
