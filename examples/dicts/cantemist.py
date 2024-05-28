import pandas as pd

def get_concept_details(cfg) -> dict:
    path = cfg.dict.custom.cantemist_path
    gazetteer_dict = pd.read_csv(path, sep="\t")

    concept_details = {}

    for _, entry in gazetteer_dict.iterrows():
        sid = str(entry['ICD-O code'])
        if sid not in concept_details:
            concept_details[sid] = {
                "concept_id": sid, 
                "canonical_name": entry['Text'], 
                "types": [], 
                "aliases": []
            }
        # Assuming "description 2" should be added to aliases if it exists
        #if not pd.isna(entry['description 2']):
            #concept_details[sid]["aliases"].append(entry['description 2'])


    return concept_details

# Example usage:
# cfg = some_configuration_object
# concept_details = get_concept_details(cfg)
# print(concept_details)