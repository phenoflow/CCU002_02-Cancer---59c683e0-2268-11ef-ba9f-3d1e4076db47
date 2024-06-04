# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"240794006","system":"icd10"},{"code":"188660004","system":"icd10"},{"code":"278055006","system":"icd10"},{"code":"107691000119101","system":"icd10"},{"code":"65399007","system":"icd10"},{"code":"109969005","system":"icd10"},{"code":"711414003","system":"icd10"},{"code":"67821000119109","system":"icd10"},{"code":"277629008","system":"icd10"},{"code":"188674006","system":"icd10"},{"code":"403923002","system":"icd10"},{"code":"443487006","system":"icd10"},{"code":"277628000","system":"icd10"},{"code":"129000002","system":"icd10"},{"code":"397009000","system":"icd10"},{"code":"188672005","system":"icd10"},{"code":"277625002","system":"icd10"},{"code":"277651000","system":"icd10"},{"code":"278057003","system":"icd10"},{"code":"118615008","system":"icd10"},{"code":"416712009","system":"icd10"},{"code":"277624003","system":"icd10"},{"code":"188668006","system":"icd10"},{"code":"723301009","system":"icd10"},{"code":"277543005","system":"icd10"},{"code":"303057009","system":"icd10"},{"code":"303055001","system":"icd10"},{"code":"188675007","system":"icd10"},{"code":"303017006","system":"icd10"},{"code":"254637007","system":"icd10"},{"code":"277653002","system":"icd10"},{"code":"188676008","system":"icd10"},{"code":"277637000","system":"icd10"},{"code":"254869000","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hepatocellular-ccu002_02-cancer---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hepatocellular-ccu002_02-cancer---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hepatocellular-ccu002_02-cancer---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
