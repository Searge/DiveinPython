class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)
        
    def __enter__(self):
        return self.f
        
    def __exit__(self, *arga):
        self.f.close()
