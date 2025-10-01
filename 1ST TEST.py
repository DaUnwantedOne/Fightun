import time
BPM = 208
beat = 60 / 208
lyrica = [
    (0.000, "Binaon naman na ang lahat"),
    (4.800, "Tinakpan naman na ‘king sugat"),
    (9.200, "Ngunit ba’t ba andito pa rin?"),
    (13, "Hirap na ‘kong intindihin"),
    (18.400, "Tanging panalangin, lubayan na sana"),
    (26.700, "Dahil sa bawat tingin, mukha mo’y nakikita"),
    (37, "Kahit sa’n man mapunta ay anino mo’y kumakapit sa'king kamay"),
    (46, "Ako ay dahan‑dahang nililibing nang buhay pa"),
    (55.20, "Hindi na makalaya, dinadalaw mo ‘ko bawat gabi"),
    (63.800, "Wala mang nakikita, haplos mo’y ramdam pa rin sa dilim"),
    (73, "Hindi na na‑nanaginip, hindi na ma‑makagising"),
    (82.70, "Pasindi na ng ilaw"),
    (87.50, "Minumulto na ‘ko ng damdamin ko, ng damdamin ko"),
    (93, "Hindi mo ba ako lilisanin?"),
    (97.500, "Hindi pa ba sapat pagpapahirap sa ‘kin?"),
    (102, "Hindi na ba ma‑mamayapa? Hindi na ba ma‑mamayapa?"),
    (111, "Hindi na makalaya, dinadalaw mo ‘ko bawat gabi"),
    (119, "Wala mang nakikita, haplos mo’y ramdam pa rin sa dilim"),
    (128, "Hindi na na‑nanaginip, hindi na ma‑makagising"),
    (138, "Pasindi na ng ilaw"),
    (142, "Minumulto na ‘ko ng damdamin ko, ng damdamin ko"),
    (149, "(Makalaya) Hindi mo ba ako lilisanin?"),
    (152, "(Dinadalaw mo ‘ko bawat gabi) Hindi pa ba sapat…"),
    (157, "(Wala mang nakikita) Hindi na ba ma‑mamayapa?"),
    (162, "(Haplos mo’y ramdam pa rin sa dilim) Hindi na ba ma‑mamayapa?")
]
def play_lyrics(lyrics):
    start = time.time()
    for ts, line in lyrics:
        while True:
            now = time.time() - start
            if now >= ts:
                print(line)
                break
                time.sleep(0.05)
if __name__ == "__main__":
    play_lyrics(lyrica)

