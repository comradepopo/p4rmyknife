import urllib.request

def run(args):
    if args.os.startswith('linux'):
      p4_url = 'http://www.perforce.com/downloads/perforce/r19.2/bin.linux26x86_64/p4v.tgz'
      urllib.request.urlretrieve(p4_url, 'p4v.tgz')
