f = open("10kMovieList.csv","r",encoding="utf8")
czyt = f.readlines()
f.close()
w = open("10kMovieList.csv","w",encoding="utf8")
for line in czyt:
    line = line.strip() + ";brak\n"
    w.write(line)
w.close()
print("done")