# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"C03","system":"icd10"},{"code":"1090921000000106","system":"icd10"},{"code":"94083008","system":"icd10"},{"code":"93941005","system":"icd10"},{"code":"94099002","system":"icd10"},{"code":"94142007","system":"icd10"},{"code":"310599006","system":"icd10"},{"code":"93842002","system":"icd10"},{"code":"93979000","system":"icd10"},{"code":"188302003","system":"icd10"},{"code":"188266000","system":"icd10"},{"code":"371979001","system":"icd10"},{"code":"1090251000000105","system":"icd10"},{"code":"188285002","system":"icd10"},{"code":"93799003","system":"icd10"},{"code":"188298006","system":"icd10"},{"code":"93814004","system":"icd10"},{"code":"188234005","system":"icd10"},{"code":"188287005","system":"icd10"},{"code":"187927003","system":"icd10"},{"code":"188264002","system":"icd10"},{"code":"363370001","system":"icd10"},{"code":"187967002","system":"icd10"},{"code":"93880001","system":"icd10"},{"code":"187932002","system":"icd10"},{"code":"94112009","system":"icd10"},{"code":"93833009","system":"icd10"},{"code":"188208002","system":"icd10"},{"code":"363477002","system":"icd10"},{"code":"93990005","system":"icd10"},{"code":"1090301000000103","system":"icd10"},{"code":"93975006","system":"icd10"},{"code":"188289008","system":"icd10"},{"code":"93677000","system":"icd10"},{"code":"93772000","system":"icd10"},{"code":"187786003","system":"icd10"},{"code":"93827000","system":"icd10"},{"code":"448674007","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-cancer-neoplasm---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-cancer-neoplasm---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-cancer-neoplasm---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
