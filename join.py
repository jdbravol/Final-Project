import os

path = os.path.join(os.getcwd() + '/processed')
print path 

def join_all_songs():
    songs = [file for file in os.listdir(path) if not file.endswith(".py")]  
    with open(os.path.join(path, "all_artists"), "wb") as output:
        for file_name in songs:
                with open(os.path.join(path, file_name), "r") as input:
                    lines = input.readlines()
                    for line in lines:
                        output.write(line)
                    input.close()
        output.close()
        
join_all_songs()