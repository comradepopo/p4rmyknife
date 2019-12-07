import urllib.request
import tarfile
import os

def run(args):
    if args.install_client:
      install_client(args)



def install_client(args):
    # Set up the p4 client environment.

    # First, download the platform-specific binary.
    if args.os.startswith('linux'):
        #p4_url = 'http://www.perforce.com/downloads/perforce/r19.2/bin.linux26x86_64/p4v.tgz'
        #The below line (line 16) is for testing purposes only, and is not intended for the final product.
        p4_url = 'https://louis-test-p4k.s3.us-east-2.amazonaws.com/p4v.tgz'
    #urllib.request.urlretrieve(p4_url, 'p4v.tgz')
    try:
        local_filename, request_headers = urllib.request.urlretrieve(p4_url,'p4v.tgz')
        html = open(local_filename)
        print (local_filename, request_headers)
        html.close()
    except:
      print ("Unable to access desired server contents.")
      #check to make sure file was successfully downloaded
    try:
        local_filename, request_headers = urllib.request.urlretrieve(p4_url,'p4v.tgz')
        html = open(local_filename)
        print (local_filename, request_headers)
        html.close()
    except:
      print ("Unable to access desired server contents.")
      sys.exit()
    try:
        f = open("p4v.tgz")
        #Perform File Operations (Reading and Writing a File)
        f.close()
    except:
        print ("File is not accessible.")
        sys.exit()

    #Get current directory
    p4vinspath = os.getcwd()
    print ("Extracting installer archive to %s" % p4vinspath)
    #Extract to said directory
    tf = tarfile.open("p4v.tgz")
    tf.extractall(p4vinspath)

    #Execute client executable- helixmfa
    exec(open("./p4v-2019.2.1883366/bin/helixmfa").read())

