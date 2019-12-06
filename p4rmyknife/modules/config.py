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

    #unzip .tgz
    if ("p4v".endswith(".tgz")):
        tar = tarfile.open("p4v", "r:tgz")
        tar.extractall()
        tar.close()
    
    
    #11/27/19 Next to add code that will execute/run the downloaded file.
