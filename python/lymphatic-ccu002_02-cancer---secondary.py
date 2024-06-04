# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"188613007","system":"icd10"},{"code":"188554007","system":"icd10"},{"code":"188500005","system":"icd10"},{"code":"93520007","system":"icd10"},{"code":"188575004","system":"icd10"},{"code":"188587006","system":"icd10"},{"code":"188551004","system":"icd10"},{"code":"188566001","system":"icd10"},{"code":"93193008","system":"icd10"},{"code":"188593003","system":"icd10"},{"code":"93135004","system":"icd10"},{"code":"188511002","system":"icd10"},{"code":"93494007","system":"icd10"},{"code":"188642004","system":"icd10"},{"code":"93521006","system":"icd10"},{"code":"188645002","system":"icd10"},{"code":"93195001","system":"icd10"},{"code":"188640007","system":"icd10"},{"code":"95186006","system":"icd10"},{"code":"93525002","system":"icd10"},{"code":"188548006","system":"icd10"},{"code":"188544008","system":"icd10"},{"code":"95224004","system":"icd10"},{"code":"93547002","system":"icd10"},{"code":"188512009","system":"icd10"},{"code":"303201005","system":"icd10"},{"code":"188579005","system":"icd10"},{"code":"188517003","system":"icd10"},{"code":"188669003","system":"icd10"},{"code":"93184007","system":"icd10"},{"code":"93542008","system":"icd10"},{"code":"94712003","system":"icd10"},{"code":"93495008","system":"icd10"},{"code":"93196000","system":"icd10"},{"code":"188493000","system":"icd10"},{"code":"188586002","system":"icd10"},{"code":"188585003","system":"icd10"},{"code":"188501009","system":"icd10"},{"code":"93133006","system":"icd10"},{"code":"188489006","system":"icd10"},{"code":"93138002","system":"icd10"},{"code":"269475001","system":"icd10"},{"code":"188572001","system":"icd10"},{"code":"188582000","system":"icd10"},{"code":"188609000","system":"icd10"},{"code":"93183001","system":"icd10"},{"code":"94709001","system":"icd10"},{"code":"93526001","system":"icd10"},{"code":"188514005","system":"icd10"},{"code":"188510001","system":"icd10"},{"code":"188559002","system":"icd10"},{"code":"188570009","system":"icd10"},{"code":"95192000","system":"icd10"},{"code":"188637007","system":"icd10"},{"code":"188590000","system":"icd10"},{"code":"93493001","system":"icd10"},{"code":"188567005","system":"icd10"},{"code":"188576003","system":"icd10"},{"code":"188515006","system":"icd10"},{"code":"94711005","system":"icd10"},{"code":"188725004","system":"icd10"},{"code":"188562004","system":"icd10"},{"code":"188662007","system":"icd10"},{"code":"93531004","system":"icd10"},{"code":"188534006","system":"icd10"},{"code":"93549004","system":"icd10"},{"code":"93137007","system":"icd10"},{"code":"188627002","system":"icd10"},{"code":"188502002","system":"icd10"},{"code":"93182006","system":"icd10"},{"code":"285644001","system":"icd10"},{"code":"95188007","system":"icd10"},{"code":"93139005","system":"icd10"},{"code":"188531003","system":"icd10"},{"code":"93191005","system":"icd10"},{"code":"109391009","system":"icd10"},{"code":"93188005","system":"icd10"},{"code":"93146001","system":"icd10"},{"code":"188565002","system":"icd10"},{"code":"93524003","system":"icd10"},{"code":"188666005","system":"icd10"},{"code":"188504001","system":"icd10"},{"code":"93192003","system":"icd10"},{"code":"188577007","system":"icd10"},{"code":"188536008","system":"icd10"},{"code":"303194003","system":"icd10"},{"code":"188538009","system":"icd10"},{"code":"93197009","system":"icd10"},{"code":"188580008","system":"icd10"},{"code":"188524002","system":"icd10"},{"code":"188569008","system":"icd10"},{"code":"188541000","system":"icd10"},{"code":"188664008","system":"icd10"},{"code":"93522004","system":"icd10"},{"code":"188507008","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lymphatic-ccu002_02-cancer---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lymphatic-ccu002_02-cancer---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lymphatic-ccu002_02-cancer---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
