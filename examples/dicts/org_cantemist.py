import pandas as pd
from collections import defaultdict
from tqdm.auto import tqdm

from xmen.log import logger
#from xmen.umls import read_umls_file_headers, get_umls_concepts

def get_concept_details(cfg) -> dict:
    path = cfg.dict.custom.cantemist_path
    gazetteer_dict = pd.read_csv(path, sep="\t")
    print(gazetteer_dict.columns)
    return {}
    gazetteer_dict.sort_values("code", inplace=True)

    concept_details = {}

    for _, entry in gazetteer_dict.iterrows():
        sid = str(entry.code)
        if not sid in concept_details:
            concept_details[sid] = {"concept_id": sid, "canonical_name": None, "types": [], "aliases": []}
        if entry.mainterm:
            assert not concept_details[sid]["canonical_name"]
            concept_details[sid]["canonical_name"] = entry.term
        else:
            concept_details[sid]["aliases"].append(entry.term)
        if entry.semantic_tag not in concept_details[sid]["types"]:
            concept_details[sid]["types"].append(entry.semantic_tag)

    for v in concept_details.values():
        if not v["canonical_name"]:
            v["canonical_name"] = v["aliases"].pop()

    return concept_details
