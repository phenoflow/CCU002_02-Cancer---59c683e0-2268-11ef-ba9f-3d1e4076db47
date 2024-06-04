# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"254988008","system":"icd10"},{"code":"408646000","system":"icd10"},{"code":"9541000119105","system":"icd10"},{"code":"399490008","system":"icd10"},{"code":"254626006","system":"icd10"},{"code":"1701000119104","system":"icd10"},{"code":"314191009","system":"icd10"},{"code":"1078901000119100","system":"icd10"},{"code":"1078881000119102","system":"icd10"},{"code":"15956341000119105","system":"icd10"},{"code":"301756000","system":"icd10"},{"code":"254917006","system":"icd10"},{"code":"309245001","system":"icd10"},{"code":"276803003","system":"icd10"},{"code":"1078961000119104","system":"icd10"},{"code":"408645001","system":"icd10"},{"code":"255110003","system":"icd10"},{"code":"449153001","system":"icd10"},{"code":"408647009","system":"icd10"},{"code":"1691000119104","system":"icd10"},{"code":"15956381000119100","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-cystadenocarcinoma---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-cystadenocarcinoma---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-cystadenocarcinoma---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
