def show_magicians(magicians_names):
    for magicians_name in magicians_names:
        print(magicians_name)

'''def make_great(magicians_names):
    for number in range(len(magicians_names)):
        magicians_names[number] = "the Great " + magicians_names[number]
    return magicians_names'''

def make_great(magicians_names):
    while magicians_names:
        current_name = "the Great" + magicians_names.pop()
        new_names.append(current_name)
    return new_names
        
new_names = []
magicians_names = ["mack","fuck","jack"]
if __name__ == "__main__":
    make_great(magicians_names[:]) #利用切片[:]来保留原列表
    show_magicians(magicians_names)
    show_magicians(new_names)

