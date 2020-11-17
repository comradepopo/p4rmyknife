import argparse
import os
import sys

# Add our modules folder to the path so we can import them.
module_path = os.path.abspath(os.path.join(__file__, '..', 'modules'))
sys.path.append(module_path)
# Import our modules.
import config


# Base argument parser definition.
parser = argparse.ArgumentParser(description='It\'s p4 - made easy.')

# Sub module parsers definition.
subparsers = parser.add_subparsers(dest='module', title='config',
                      description='commands for working configuring p4',
                      help='config help')



# Sub module parser and arguement definitions.
config_parser = subparsers.add_parser('config')
config_parser.add_argument('--install-client', action='store_true',
                    help='install client environment')


#this is a comment

# Set some defaults that are used by all sub modules
parser.set_defaults(os=sys.platform)


# Run the parsing to create our namespace args.
args = parser.parse_args()

# Call the "run" method of the appropriate module.
if args.module == 'config':
    config.run(args)
elif args.module == 'replication':
    print('Not yet implemented.')
elif args.module == 'migration':
    print('Not yet implemented.')
