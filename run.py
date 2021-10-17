from argparse import ArgumentParser
import shutil
import os, sys

MVTN_VERSION = "0.1"

def main():
    global MVTN_VERSION

    parser = ArgumentParser(description='Mvtn scalability test')
    parser.add_argument('action', help='action to execute', choices=[
        'run', 'clean'
    ])
    parser.add_argument('--config', help='Config file name (see generator/config folder)',
                        default='heavy_note_taker')
    parser.add_argument('-e', '--emacs', type=str, help='emacs executable',
                        default='emacs')
    parser.add_argument('--skip-generator', action="store_true",
                        help='Skip note generator')
    parser.add_argument('--clean', action="store_true", help='Clean this repository')

    try: args = parser.parse_args()
    except: sys.exit(1)

    if args.action == 'clean':
        try: os.remove('emacs-config' + os.sep + 'mvtn.tar')
        except: pass
        shutil.rmtree('emacs-config' + os.sep + 'elpa', ignore_errors=True)
        shutil.rmtree('test-notes' + os.sep + 'prv', ignore_errors=True)
        shutil.rmtree('test-notes' + os.sep + 'wrk', ignore_errors=True)
        prevdir = os.getcwd(); os.chdir("mvtn.el")
        os.system("make clean")
        os.chdir(prevdir)
    elif args.action == 'run':
        prevdir = os.getcwd(); os.chdir("mvtn.el")
        os.system("make package")
        os.chdir(prevdir)
        shutil.copyfile('mvtn.el' + os.sep + f'mvtn-{MVTN_VERSION}.tar',
                        'emacs-config' + os.sep + 'mvtn.tar')

        if not args.skip_generator:
            os.system('python3 generator' + os.sep + 'generate_test_notes.py ' + args.config)
        else: print("Skipping note generation")

        os.system(args.emacs + ' -Q -L mvtn.el -l emacs-config/init.el')


if __name__ == '__main__': main()
