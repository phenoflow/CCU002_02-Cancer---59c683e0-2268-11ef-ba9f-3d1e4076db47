# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"277549009","system":"icd10"},{"code":"188732008","system":"icd10"},{"code":"188734009","system":"icd10"},{"code":"277571004","system":"icd10"},{"code":"307617006","system":"icd10"},{"code":"92818009","system":"icd10"},{"code":"699818003","system":"icd10"},{"code":"413847001","system":"icd10"},{"code":"277574007","system":"icd10"},{"code":"110006004","system":"icd10"},{"code":"110007008","system":"icd10"},{"code":"91855006","system":"icd10"},{"code":"413441006","system":"icd10"},{"code":"188728002","system":"icd10"},{"code":"277575008","system":"icd10"},{"code":"277573001","system":"icd10"},{"code":"277473004","system":"icd10"},{"code":"92812005","system":"icd10"},{"code":"188744006","system":"icd10"},{"code":"359631009","system":"icd10"},{"code":"110002002","system":"icd10"},{"code":"91861009","system":"icd10"},{"code":"277569004","system":"icd10"},{"code":"314418005","system":"icd10"},{"code":"188754005","system":"icd10"},{"code":"161436008","system":"icd10"},{"code":"92814006","system":"icd10"},{"code":"277572006","system":"icd10"},{"code":"188741003","system":"icd10"},{"code":"118613001","system":"icd10"},{"code":"277601005","system":"icd10"},{"code":"277567002","system":"icd10"},{"code":"95210003","system":"icd10"},{"code":"190030009","system":"icd10"},{"code":"302855005","system":"icd10"},{"code":"277587001","system":"icd10"},{"code":"278453007","system":"icd10"},{"code":"188726003","system":"icd10"},{"code":"277604002","system":"icd10"},{"code":"188745007","system":"icd10"},{"code":"91857003","system":"icd10"},{"code":"277602003","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["aleukemic-ccu002_02-cancer---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["aleukemic-ccu002_02-cancer---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["aleukemic-ccu002_02-cancer---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
