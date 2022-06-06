class map():
    def __init__(self):
        pass
    def load_map(path):
        f = open(path + '.txt','r')
        data = f.read()
        f.close()
        data = data.split('\n')
        tilemap = []
        for row in data:
            tilemap.append(list(row))
        return tilemap

