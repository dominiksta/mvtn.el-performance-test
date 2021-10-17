import os, sys
import datetime
import random
import textwrap
import shutil
import importlib
from argparse import ArgumentParser

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------

BASE_DIR = os.path.dirname(__file__) + os.sep + '..' + os.sep + 'test-notes'

_LOREM_IPSUM = """\
Nullam eu ante vel est convallis dignissim.  Fusce suscipit, wisi nec facilisis
facilisis, est dui fermentum leo, quis tempor ligula erat quis odio.  Nunc porta
vulputate tellus.  Nunc rutrum turpis sed pede.  Sed bibendum.  Aliquam posuere.
Nunc aliquet, augue nec adipiscing interdum, lacus tellus malesuada massa, quis
varius mi purus non odio.  Pellentesque condimentum, magna ut suscipit
hendrerit, ipsum augue ornare nulla, non luctus diam neque sit amet urna.
Curabitur vulputate vestibulum lorem.  Fusce sagittis, libero non molestie
mollis, magna orci ultrices dolor, at vulputate neque nulla lacinia eros.  Sed
id ligula quis est convallis tempor.  Curabitur lacinia pulvinar nibh.  Nam a
sapien.
"""

# ----------------------------------------------------------------------
# Code
# ----------------------------------------------------------------------

def note_string(
        id_prefix: str, number: int, link_amount_max: int, lorem_ipsum_max: int,
        template: str
) -> str:
    """
    Generate a note as a string from template.
    - NUMBER specifies the id the note should have (000000-{number:06d})
    - link_amount_max specifies the maximum amount of other notes the generated
      note should link to
    - lorem_ipsum_max specifies the maxmium number of paragraphs the note should
      include after the links
    """
    global _LOREM_IPSUM

    date = '{0:%Y-%m-%d}'.format(datetime.datetime.now())

    link_amount = random.randint(0, link_amount_max)
    links = ''
    for i in range(number + 1, number + link_amount + 1):
        links += f'- ^^{id_prefix}-{i:06d} Test note {i}^^\n'

    lorem_ipsum = random.randint(1, lorem_ipsum_max)
    lorem_ipsums = ''
    for i in range(0, lorem_ipsum): lorem_ipsums += _LOREM_IPSUM + '\n'

    template_vars = {
        'number': number, 'date': date, 'links': links,
        'lorem_ipsums': lorem_ipsums,
    }

    return template.format(**template_vars)


def generate_note_files(
        target_dir: str, id_prefix: str, amount: int, link_amount_max: int,
        lorem_ipsum_max: int, template: str
) -> None:
    """
    """
    prevdir = os.getcwd();
    if not os.path.exists(target_dir): os.makedirs(target_dir, exist_ok=True)
    os.chdir(target_dir)

    for i in range(0, amount):
        filename = f'{id_prefix}-{i:06d} Test Note {i}.org' 
        # print(f"-> writing {target_dir}/{filename}")
        with open(filename, 'w') as file:
            file.write(note_string(
                id_prefix, i, link_amount_max, lorem_ipsum_max, template
            ))

    os.chdir(prevdir)


def main():
    parser = ArgumentParser(description='Generator for Mvtn Test-Notes')
    parser.add_argument('config', help='Config file name (see config folder)')

    try: args = parser.parse_args()
    except: sys.exit(1)

    config = importlib.import_module('config.' + args.config).config

    if os.path.exists(BASE_DIR): shutil.rmtree(BASE_DIR)
    os.mkdir(BASE_DIR)
    prevdir = os.getcwd(); os.chdir(BASE_DIR)

    print("Generating test notes...")
    for year in reversed(range(2021 - config['years'], 2021)):
        for key in config['note_directories']:
            nd = config['note_directories'][key]
            generate_note_files(
                target_dir = key if nd['static'] else key + '/' + str(year),
                id_prefix = str(year) + nd['id_prefix_day'],
                amount = nd['generation']['notes_per_year'],
                link_amount_max = nd['generation']['max_links_per_note'],
                lorem_ipsum_max = nd['generation']['max_paragraphs_per_note'],
                template=config['template']
            )
    print("done")

    os.chdir(prevdir)


if __name__ == '__main__': main()