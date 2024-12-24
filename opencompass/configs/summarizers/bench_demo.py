from mmengine.config import read_base

with read_base():
    from .groups.mmlu import mmlu_summary_groups
    from .groups.cmmlu import cmmlu_summary_groups


other_summary_groups = []
other_summary_groups.append({'name': 'Exam', 'subsets': ['mmlu','cmmlu']})

other_summary_groups.append({'name': 'Overall', 'subsets': ['Exam']})

summarizer = dict(
    dataset_abbrs=[
        'Overall',
        'Exam',
        '--------- 考试 Exam ---------',  # category
        # 'Mixed', # subcategory
        'mmlu',
        'cmmlu',
    ],
    summary_groups=sum(
        [v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)