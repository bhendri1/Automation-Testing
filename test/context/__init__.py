class Context:
    def __init__(self):
        self.attributes = {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass

    def __getattr__(self, name):
        return self.attributes.get(name, None)
    
    def __setattr__(self, name, value):
        if name == 'attributes':
            super(Context, self).__setattr__(name, value)
        else:
            self.attributes[name] = value
