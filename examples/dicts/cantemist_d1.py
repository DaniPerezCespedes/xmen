import pandas as pd

def get_concept_details(cfg) -> dict:
    path = cfg.dict.custom.cantemist_path
    gazetteer_dict = pd.read_csv(path, sep="\t")

    concept_details = {}

    #Add to knowledge base only the ICD-O codes from official terminology
    for _, entry in gazetteer_dict.iterrows():
        sid = str(entry['ICD-O code'])
        if sid not in concept_details:
            concept_details[sid] = {
                "concept_id": sid, 
                "canonical_name": entry['Description 1'], 
                "types": [], 
                "aliases": []
            }
        
        if cfg.dict.custom.get("include_h_codes", False):
            #Add an H to the end of the code (special cases when SAI cannot be used, and refers to "son of..." = "hijo de..")    
            sid_h = str(entry['ICD-O code']) + "/H"
            if sid_h not in concept_details:
                concept_details[sid_h] = {
                    "concept_id": sid_h, 
                    "canonical_name": "hijo de " + entry['Description 1'], 
                    "types": [], 
                    "aliases": [],
                }
         
        if cfg.dict.custom.get("include_grades", False):
            #Add the grade 1 to all the concepts at the end --> for a code such as 8000/11 it will be redundant, because it will have 3 ones (or 3 digits after the /, which doesn't exist
            sid_grade1 = str(entry['ICD-O code']) + "1"
            if sid_grade1 not in concept_details:
                concept_details[sid_grade1] = {
                    "concept_id": sid_grade1, 
                    "canonical_name": entry['Description 1'] + " de bajo grado", 
                    "types": [], 
                    "aliases": [],
                }

            #Add the grade 2 to all the concepts at the end
            sid_grade2 = str(entry['ICD-O code']) + "2"
            if sid_grade2 not in concept_details:
                concept_details[sid_grade2] = {
                    "concept_id": sid_grade2, 
                    "canonical_name": entry['Description 1'] + " de grado intermedio", 
                    "types": [], 
                    "aliases": [],
                }

            #Add the grade 3 to all the concepts at the end
            sid_grade3 = str(entry['ICD-O code']) + "3"
            if sid_grade3 not in concept_details:
                concept_details[sid_grade3] = {
                    "concept_id": sid_grade3, 
                    "canonical_name": entry['Description 1'] + " de grado intermedio", 
                    "types": [], 
                    "aliases": [],
                }

            #Add the grade 4 to all the concepts at the end
            sid_grade4 = str(entry['ICD-O code']) + "4"
            if sid_grade4 not in concept_details:
                concept_details[sid_grade4] = {
                    "concept_id": sid_grade4, 
                    "canonical_name": entry['Description 1'] + " de alto grado", 
                    "types": [], 
                    "aliases": [],
                }  

        if cfg.dict.custom.get("include_grades_v2", False):
            
            #a) Grade 1, according to level, differentiation, number, roman number
            sid_grade1a = str(entry['ICD-O code']) + "1"
            if sid_grade1a not in concept_details:
                concept_details[sid_grade1a] = {
                    "concept_id": sid_grade1a, 
                    "canonical_name": entry['Description 1'] + " de bajo grado", 
                    "types": [], 
                    "aliases": [
                        entry['Description 1'] + " bien diferenciado",
                        entry['Description 1'] + " grado 1",
                        entry['Description 1'] + " grado I"
                    ],
                }
            #b) Grade 2, according to level, differentiation, number, roman number
            sid_grade2a = str(entry['ICD-O code']) + "2"
            if sid_grade2a not in concept_details:
                concept_details[sid_grade2a] = {
                    "concept_id": sid_grade2a, 
                    "canonical_name": entry['Description 1'] + " de grado intermedio", 
                    "types": [], 
                    "aliases": [
                        entry['Description 1'] + " moderadamente diferenciado",
                        entry['Description 1'] + " grado 2",
                        entry['Description 1'] + " grado II"
                    ],
                }
            #c) Grade 3, according to level, differentiation, number, roman number
            sid_grade3a = str(entry['ICD-O code']) + "3"
            if sid_grade3a not in concept_details:
                concept_details[sid_grade3a] = {
                    "concept_id": sid_grade3a, 
                    "canonical_name": entry['Description 1'] + " de grado intermedio", 
                    "types": [], 
                    "aliases": [
                        entry['Description 1'] + " pobremente diferenciado",
                        entry['Description 1'] + " poco diferenciado",
                        entry['Description 1'] + " mal diferenciado",
                        entry['Description 1'] + " grado 3",
                        entry['Description 1'] + " grado III"
                    ],
                }        
            #d) Grade 4, according to level, differentiation, number, roman number
            sid_grade4a = str(entry['ICD-O code']) + "4"
            if sid_grade4a not in concept_details:
                concept_details[sid_grade4a] = {
                    "concept_id": sid_grade4a, 
                    "canonical_name": entry['Description 1'] + " de alto grado", 
                    "types": [], 
                    "aliases": [
                        entry['Description 1'] + " indiferenciado",
                        entry['Description 1'] + " grado 4",
                        entry['Description 1'] + " grado IV"
                    ],
                }  
  
    if path2 := cfg.dict.custom.get("custom_codes_path", None):
        # Process entries from the second TSV file
        gazetteer_dict2 = pd.read_csv(path2, sep="\t")   
        for _, entry in gazetteer_dict2.iterrows():
            sid = str(entry['ICD-O code'])
            if sid not in concept_details:
                concept_details[sid] = {
                    "concept_id": sid, 
                    "canonical_name": entry['Description 1'], 
                    "types": [], 
                    "aliases": []
                }
    if path3 := cfg.dict.custom.get("custom_codes_path_2", None):
        # Process entries from the second TSV file
        gazetteer_dict3 = pd.read_csv(path3, sep="\t")   
        for _, entry in gazetteer_dict3.iterrows():
            sid = str(entry['ICD-O code'])
            if sid not in concept_details:
                concept_details[sid] = {
                    "concept_id": sid, 
                    "canonical_name": entry['Description 1'], 
                    "types": [], 
                    "aliases": []
                }                   
    return concept_details

# Example usage:
# cfg = some_configuration_object
# concept_details = get_concept_details(cfg)
# print(concept_details)