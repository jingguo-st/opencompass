subcategories = {
    'agronomy': ['other'],
}

categories = {
    'Other':['other'],
}

category2subject = {}
for k, v in categories.items():
    for subject, subcat in subcategories.items():
        for c in subcat:
            if c in v:
                category2subject.setdefault(k, []).append(subject)

cmmlu_summary_groups = []

_cmmlu_other = ['cmmlu-' + s for s in category2subject['Other']]
cmmlu_summary_groups.append({'name': 'cmmlu-other', 'subsets': _cmmlu_other})

_cmmlu_all = ['cmmlu-' + s for s in subcategories.keys()]
cmmlu_summary_groups.append({'name': 'cmmlu', 'subsets': _cmmlu_all})
