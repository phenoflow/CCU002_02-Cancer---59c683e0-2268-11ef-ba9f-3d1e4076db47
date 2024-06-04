# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"C63","system":"icd10"},{"code":"C02","system":"icd10"},{"code":"C49","system":"icd10"},{"code":"C06","system":"icd10"},{"code":"C57","system":"icd10"},{"code":"C44","system":"icd10"},{"code":"394895009","system":"icd10"},{"code":"829591000000101","system":"icd10"},{"code":"315601005","system":"icd10"},{"code":"265761001","system":"icd10"},{"code":"268500004","system":"icd10"},{"code":"169403005","system":"icd10"},{"code":"169402000","system":"icd10"},{"code":"367336001","system":"icd10"},{"code":"394894008","system":"icd10"},{"code":"169396008","system":"icd10"},{"code":"169401007","system":"icd10"},{"code":"396181000000106","system":"icd10"},{"code":"235391000000102","system":"icd10"},{"code":"232681000000103","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-radiochemotherapy---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-radiochemotherapy---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-radiochemotherapy---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
