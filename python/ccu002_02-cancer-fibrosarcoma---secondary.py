# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"C46","system":"icd10"},{"code":"231835006","system":"icd10"},{"code":"307219002","system":"icd10"},{"code":"424952003","system":"icd10"},{"code":"254800003","system":"icd10"},{"code":"255114007","system":"icd10"},{"code":"278046008","system":"icd10"},{"code":"254897006","system":"icd10"},{"code":"109388009","system":"icd10"},{"code":"188029000","system":"icd10"},{"code":"255067005","system":"icd10"},{"code":"443144000","system":"icd10"},{"code":"254748009","system":"icd10"},{"code":"109385007","system":"icd10"},{"code":"253042009","system":"icd10"},{"code":"109392002","system":"icd10"},{"code":"94719007","system":"icd10"},{"code":"302851001","system":"icd10"},{"code":"187822008","system":"icd10"},{"code":"109386008","system":"icd10"},{"code":"188738007","system":"icd10"},{"code":"424413001","system":"icd10"},{"code":"699357004","system":"icd10"},{"code":"254601002","system":"icd10"},{"code":"278050001","system":"icd10"},{"code":"276799004","system":"icd10"},{"code":"724649000","system":"icd10"},{"code":"254877001","system":"icd10"},{"code":"254918001","system":"icd10"},{"code":"449101009","system":"icd10"},{"code":"118606001","system":"icd10"},{"code":"307608006","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-fibrosarcoma---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-fibrosarcoma---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-fibrosarcoma---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
