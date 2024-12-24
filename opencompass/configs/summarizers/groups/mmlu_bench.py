mmlu_summary_groups = []

_mmlu_stem = ['college_biology', 'college_chemistry']
_mmlu_stem = ['lukaemon_mmlu_' + s for s in _mmlu_stem]
mmlu_summary_groups.append({'name': 'mmlu-stem', 'subsets': _mmlu_stem})

_mmlu_all = _mmlu_stem
_mmlu_weights = {'college_biology': 144,'college_chemistry': 100}
_mmlu_weights = {'lukaemon_mmlu_' + k : v for k,v in _mmlu_weights.items()}
mmlu_summary_groups.append({'name': 'mmlu', 'subsets': _mmlu_all})
mmlu_summary_groups.append({'name': 'mmlu-weighted', 'subsets': _mmlu_all, 'weights': _mmlu_weights})