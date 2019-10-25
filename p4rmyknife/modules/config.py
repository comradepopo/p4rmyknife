import urllib.request

def run(args):
    if args.install_client:
      install_client(args)



def install_client(args):
    # Set up the p4 client environment.

    # First, download the platform-specific binary.
    if args.os.startswith('linux'):
      #p4_url = 'http://www.perforce.com/downloads/perforce/r19.2/bin.linux26x86_64/p4v.tgz'
      #The below line (line 16) is for testing purposes only, and is not intended for the final product.
       p4_url = 'https://louis-test-p4k.s3.us-east-2.amazonaws.com/TestFile.sh'
      urllib.request.urlretrieve(p4_url, 'p4v.tgz')
