config = {
    'years': 10,
    'template': """\
#+TITLE: Test Note {number}
#+DATE: {date}
# mvtn_original_title :: Test Note {number}
# mvtn_original_id :: 00000000-{number:06d}

Links:
{links}

{lorem_ipsums}
""",
    'note_directories': {
        # fleeting
        'prv/flt': {
            'static': False,
            'id_prefix_day': '0000',
            'generation': {
                'notes_per_year':  100,
                'max_paragraphs_per_note':  5,
                'max_links_per_note':  3,
            },
        },
        # technical notes
        'prv/tec': {
            'static': False,
            'id_prefix_day': '0002',
            'generation': {
                'notes_per_year':  50,
                'max_paragraphs_per_note':  5,
                'max_links_per_note':  3,
            },
        },
        # static (non-datetree)
        'prv/stc': {
            'static': True,
            'id_prefix_day': '0003',
            'generation': {
                'notes_per_year':  3,
                'max_paragraphs_per_note':  20,
                'max_links_per_note':  10,
            },
        },
        # work fleeting
        'wrk/flt': {
            'static': False,
            'id_prefix_day': '0010',
            'generation': {
                'notes_per_year':  100,
                'max_paragraphs_per_note':  5,
                'max_links_per_note':  3,
            },
        },
        # work static
        'wrk/stc': {
            'static': True,
            'id_prefix_day': '0010',
            'generation': {
                'notes_per_year':  3,
                'max_paragraphs_per_note':  10,
                'max_links_per_note':  5,
            },
        },
    }
}