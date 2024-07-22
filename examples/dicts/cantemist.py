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
                "aliases": [entry['Description 2']]
            }
        
        if cfg.dict.custom.get("include_h_codes", False):
            #Add an H to the end of the code (special cases when SAI cannot be used, and refers to "son of..." = "hijo de..")    
            sid_h = str(entry['ICD-O code']) + "/H"
            if sid_h not in concept_details:
                concept_details[sid_h] = {
                    "concept_id": sid_h, 
                    "canonical_name": "hijo de " + entry['Description 1'], 
                    "types": [], 
                    "aliases": ["hijo de "+ entry['Description 2']],
                }
         
        if cfg.dict.custom.get("include_grades", False):
            #Add the grade 1 to all the concepts at the end --> for a code such as 8000/11 it will be redundant, because it will have 3 ones (or 3 digits after the /, which doesn't exist
            sid_grade1 = str(entry['ICD-O code']) + "1"
            if sid_grade1 not in concept_details:
                concept_details[sid_grade1] = {
                    "concept_id": sid_grade1, 
                    "canonical_name": entry['Description 1'] + " de bajo grado", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " de bajo grado"],
                }

            #Add the grade 2 to all the concepts at the end
            sid_grade2 = str(entry['ICD-O code']) + "2"
            if sid_grade2 not in concept_details:
                concept_details[sid_grade2] = {
                    "concept_id": sid_grade2, 
                    "canonical_name": entry['Description 1'] + " de grado intermedio", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " de grado intermedio"],
                }

            #Add the grade 3 to all the concepts at the end
            sid_grade3 = str(entry['ICD-O code']) + "3"
            if sid_grade3 not in concept_details:
                concept_details[sid_grade3] = {
                    "concept_id": sid_grade3, 
                    "canonical_name": entry['Description 1'] + " grado 3", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " grado 3"],
                }

            #Add the grade 4 to all the concepts at the end
            sid_grade4 = str(entry['ICD-O code']) + "4"
            if sid_grade4 not in concept_details:
                concept_details[sid_grade4] = {
                    "concept_id": sid_grade4, 
                    "canonical_name": entry['Description 1'] + " de alto grado", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " de alto grado"],
                }  
        if cfg.dict.custom.get("include_grades_v2", False):
            #Add the grade 1 to all the concepts at the end of the code
            #a) Add description according to the grade
            sid_grade1a = str(entry['ICD-O code']) + "1"
            if sid_grade1a not in concept_details:
                concept_details[sid_grade1a] = {
                    "concept_id": sid_grade1a, 
                    "canonical_name": entry['Description 1'] + " de bajo grado", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " de bajo grado"],
                }
            #b) Add differentiation according to the grade
            sid_grade1b = str(entry['ICD-O code']) + "1"
            if sid_grade1b not in concept_details:
                concept_details[sid_grade1b] = {
                    "concept_id": sid_grade1b, 
                    "canonical_name": entry['Description 1'] + " bien diferenciado", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " bien diferenciado"],
                }           
           #c) Add grade 1
            sid_grade1c = str(entry['ICD-O code']) + "1"
            if sid_grade1c not in concept_details:
                concept_details[sid_grade1c] = {
                    "concept_id": sid_grade1c, 
                    "canonical_name": entry['Description 1'] + " grado 1", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " grado 1"],
                }
            #d) Add grade I
            sid_grade1d = str(entry['ICD-O code']) + "1"
            if sid_grade1d not in concept_details:
                concept_details[sid_grade1d] = {
                    "concept_id": sid_grade1d, 
                    "canonical_name": entry['Description 1'] + " grado I", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " grado I"],
                }
            #Add the grade 2 to all the concepts at the end of the code
            #a) Add description according to the grade
            sid_grade2a = str(entry['ICD-O code']) + "2"
            if sid_grade2a not in concept_details:
                concept_details[sid_grade2a] = {
                    "concept_id": sid_grade2a, 
                    "canonical_name": entry['Description 1'] + " de grado intermedio", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " de grado intermedio"],
                }
            #b) Add differentiation according to the grade
            sid_grade2b = str(entry['ICD-O code']) + "2"
            if sid_grade2b not in concept_details:
                concept_details[sid_grade2b] = {
                    "concept_id": sid_grade2b, 
                    "canonical_name": entry['Description 1'] + " moderadamente diferenciado", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " moderadamente diferenciado"],
                }           
            #c) Add grade 2
            
            sid_grade2c = str(entry['ICD-O code']) + "2"
            if sid_grade2c not in concept_details:
                concept_details[sid_grade2c] = {
                    "concept_id": sid_grade2c, 
                    "canonical_name": entry['Description 1'] + " grado 2", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " grado 2"],
                }
            #d) Add grade II
            sid_grade2d = str(entry['ICD-O code']) + "2"
            if sid_grade2d not in concept_details:
                concept_details[sid_grade2d] = {
                    "concept_id": sid_grade2d, 
                    "canonical_name": entry['Description 1'] + " grado II", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " grado II"],
                }
               
            #Add the grade 3 to all the concepts at the end of the code
            #a) Add description according to the grade
            sid_grade3a = str(entry['ICD-O code']) + "3"
            if sid_grade3a not in concept_details:
                concept_details[sid_grade3a] = {
                    "concept_id": sid_grade3a, 
                    "canonical_name": entry['Description 1'] + " de grado intermedio", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " de grado intermedio"],
                }

            
            #b) Add differentiation according to the grade
            sid_grade3b1 = str(entry['ICD-O code']) + "3"
            if sid_grade3b1 not in concept_details:
                concept_details[sid_grade3b1] = {
                    "concept_id": sid_grade3b1, 
                    "canonical_name": entry['Description 1'] + " pobremente diferenciado", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " pobremente diferenciado"],
                }   
            sid_grade3b2 = str(entry['ICD-O code']) + "3"
            if sid_grade3b2 not in concept_details:
                concept_details[sid_grade3b2] = {
                    "concept_id": sid_grade3b2, 
                    "canonical_name": entry['Description 1'] + " poco diferenciado", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " poco diferenciado"],
                } 
            sid_grade3b3 = str(entry['ICD-O code']) + "3"
            if sid_grade3b3 not in concept_details:
                concept_details[sid_grade3b3] = {
                    "concept_id": sid_grade3b3, 
                    "canonical_name": entry['Description 1'] + " mal diferenciado", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " mal diferenciado"],
                }   
            #c) Add grade 3
            
            sid_grade3c = str(entry['ICD-O code']) + "3"
            if sid_grade3c not in concept_details:
                concept_details[sid_grade3c] = {
                    "concept_id": sid_grade3c, 
                    "canonical_name": entry['Description 1'] + " grado 3", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " grado 3"],
                }
            #d) Add grade III
            sid_grade3d = str(entry['ICD-O code']) + "3"
            if sid_grade3d not in concept_details:
                concept_details[sid_grade3d] = {
                    "concept_id": sid_grade3d, 
                    "canonical_name": entry['Description 1'] + " grado III", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " grado III"],
                }

            #Add the grade 4 to all the concepts at the end of the code
            #a) Add description according to the grade
            sid_grade4a = str(entry['ICD-O code']) + "4"
            if sid_grade4a not in concept_details:
                concept_details[sid_grade4a] = {
                    "concept_id": sid_grade4a, 
                    "canonical_name": entry['Description 1'] + " de alto grado", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " de alto grado"],
                }
                
            #b) Add differentiation according to the grade
            sid_grade4b = str(entry['ICD-O code']) + "4"
            if sid_grade2b not in concept_details:
                concept_details[sid_grade4b] = {
                    "concept_id": sid_grade4b, 
                    "canonical_name": entry['Description 1'] + " indiferenciado", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " indiferenciado"],
                }           
            #c) Add grade 4
            sid_grade4c = str(entry['ICD-O code']) + "4"
            if sid_grade4c not in concept_details:
                concept_details[sid_grade4c] = {
                    "concept_id": sid_grade4c, 
                    "canonical_name": entry['Description 1'] + " grado 4", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " grado 4"],
                }
            #d) Add grade IV
    
            sid_grade4d = str(entry['ICD-O code']) + "4"
            if sid_grade4d not in concept_details:
                concept_details[sid_grade4d] = {
                    "concept_id": sid_grade4d, 
                    "canonical_name": entry['Description 1'] + " grado IV", 
                    "types": [], 
                    "aliases": [entry['Description 2'] + " grado IV"],
                }

    
    if path2 := cfg.dict.custom.get("custom_codes_path", None):
        # Process entries from the second TSV file (c
        gazetteer_dict2 = pd.read_csv(path2, sep="\t")   
        for _, entry in gazetteer_dict2.iterrows():
            sid = str(entry['ICD-O code'])
            if sid not in concept_details:
                concept_details[sid] = {
                    "concept_id": sid, 
                    "canonical_name": entry['Description 1'], 
                    "types": [], 
                    "aliases": [entry['Description 2']]
                }
                   
    return concept_details

# Example usage:
# cfg = some_configuration_object
# concept_details = get_concept_details(cfg)
# print(concept_details)