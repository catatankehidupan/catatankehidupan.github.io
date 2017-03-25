import glob, re

lokasi = "/sdcard/Git/catatan-kehidupan/"
home = open(lokasi+"index.html", "w")
header1 = open(lokasi+"_komponen/header1.txt").read()
header2 = open(lokasi+"_komponen/header2.txt").read()
header3 = open(lokasi+"_komponen/header3.txt").read()
footer = open(lokasi+"_komponen/footer.txt").read()
data = open(lokasi+"html/bin/data.js", "w")
dataawal = open(lokasi+"_komponen/data awal.txt").read()
dataakhir = open(lokasi+"_komponen/data akhir.txt").read()
data1 = open(lokasi+"_komponen/data1.txt").read()
data2 = open(lokasi+"_komponen/data2.txt").read()
data3 = open(lokasi+"_komponen/data3.txt").read()

postingan = glob.glob(lokasi+"post/*.md")
# print postingan
fpostingan = postingan[:]
target = postingan[:]
judul = postingan[:]
for n, x in enumerate(target):
    target[n] = re.sub(r"/post/", r"/html/", target[n])
    target[n] = re.sub(r" ", r"-", target[n])
    target[n] = target[n][:-3] + ".html"
# print target
link = target[:]
for n, x in enumerate(judul):
    judul[n] = re.sub(r""+lokasi+"post/", r"", judul[n])
    judul[n] = re.sub(r".md", r"", judul[n])
    judul[n] = judul[n].title()
print judul
for n, x in enumerate(postingan):
    fpostingan[n] = []
    fpostingan[n].append(header1)
    fpostingan[n].append(judul[n])
    fpostingan[n].append(header2)
    fpostingan[n].append(judul[n])
    fpostingan[n].append(header3)
    fpostingan[n].append(open(x).read())
    fpostingan[n].append(footer)
    fpostingan[n] = "".join(str(x) for x in fpostingan[n])
    open(target[n], "w").write(fpostingan[n])
for n, x in enumerate(link):
    link[n] = re.sub(r""+lokasi+"html/", r"", link[n])
# print link
home.write("<script>location.href='html/"+link[0]+"'</script>")
inputdata = dataawal
for n, x in enumerate(judul):
    inputdata += data1
    inputdata += x
    inputdata += data2
    inputdata += link[n]
    inputdata += data3
inputdata += dataakhir
data.write(inputdata)