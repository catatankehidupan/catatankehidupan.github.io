import glob, re, random, string

lokasi = "/sdcard/Git/catatan-kehidupan/"

index = open(lokasi+"index.html", "w")
konten = open(lokasi+"_template/konten.txt").read()
konten = string.Template(konten)

postingan = glob.glob(lokasi+"post/*.md")
fpostingan = postingan[:]
target = postingan[:]
judul = postingan[:]

for n, x in enumerate(target):
    target[n] = re.sub(r"/post/", r"/html/", target[n])
    target[n] = re.sub(r" ", r"-", target[n])
    target[n] = target[n][:-3] + ".html"
link = target[:]
for n, x in enumerate(judul):
    judul[n] = re.sub(r""+lokasi+"post/", r"", judul[n])
    judul[n] = re.sub(r".md", r"", judul[n])
    judul[n] = judul[n].title()
for n, x in enumerate(link):
    link[n] = re.sub(r""+lokasi+"html/", r"", link[n])
more = []
for n, x in enumerate(judul):
    more.append(judul[n]+"gebfhahs"+link[n])
more = [x.split("gebfhahs") for x in more]
for n, x in enumerate(postingan):
    random.shuffle(more)
    title = judul[n]
    isi = open(x).read()
    judul1 = more[0][0]
    judul2 = more[1][0]
    judul3 = more[2][0]
    link1 = more[0][1]
    link2 = more[1][1]
    link3 = more[2][1]
    dict = {
    	    "title": title,
    	    "isi": isi,
    	    "judul1": judul1,
    	    "judul2": judul2,
    	    "judul3": judul3,
    	    "link1": link1,
    	    "link2": link2,
    	    "link3": link3
    	}
    hasil = konten.substitute(dict)
    open(target[n], "w").write(hasil)
banyak = len(link)
banyak = random.randrange(banyak)
index.write("<script>location.href='html/"+link[banyak]+"'</script>")
for n, x in enumerate(judul):
    print str(n+1)+". ",
    print x