# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"187722004","system":"icd10"},{"code":"417036008","system":"icd10"},{"code":"187989003","system":"icd10"},{"code":"93779009","system":"icd10"},{"code":"254535007","system":"icd10"},{"code":"1090141000000102","system":"icd10"},{"code":"1090131000000106","system":"icd10"},{"code":"372097009","system":"icd10"},{"code":"1090121000000109","system":"icd10"},{"code":"188177003","system":"icd10"},{"code":"188183000","system":"icd10"},{"code":"187916000","system":"icd10"},{"code":"188176007","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["endocervical-ccu002_02-cancer---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["endocervical-ccu002_02-cancer---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["endocervical-ccu002_02-cancer---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
