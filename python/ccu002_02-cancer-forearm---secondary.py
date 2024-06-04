# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"C30","system":"icd10"},{"code":"188061001","system":"icd10"},{"code":"187994003","system":"icd10"},{"code":"269463006","system":"icd10"},{"code":"187993009","system":"icd10"},{"code":"187929000","system":"icd10"},{"code":"187828007","system":"icd10"},{"code":"188062008","system":"icd10"},{"code":"188032002","system":"icd10"},{"code":"363359008","system":"icd10"},{"code":"187987001","system":"icd10"},{"code":"255073006","system":"icd10"},{"code":"277156006","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-forearm---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-forearm---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-forearm---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
