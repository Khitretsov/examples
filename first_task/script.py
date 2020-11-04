obj = {
    'a': 1,
    'b': 3,
    'c': {
        'd': 2,
        'a': 3,
        'f': {
            'f': 2,
            'd':3
        },
        'v': 4
    }
}   

def flatten(d):
    answer = {}
    
    def search_path(dd, letter=''):
        paths = []
        keys = dd.keys()
        for key in keys:
            field = key if letter == '' else letter + '.' + key
            try:
                hash(dd[key])
                answer[field] = dd[key]
            except:
                search_path(dd[key], field)
                
        
    search_path(d)
    print(answer)
    return answer


flatten(obj)