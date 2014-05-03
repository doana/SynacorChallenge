class VM:
 
    def __init__(self, binary, logger):
        self.binary = binary
        self.logger = logger

    def run(self):
        print "Running!" 
