def ubahFacebook(kalimat):
    if kalimat == "Face" or kalimat == "FB" or kalimat == "Fesbuk":
        return "Facebook"
    else:
        return kalimat

kalimat = ["Face", "halo"]

facebook = map(ubahFacebook, kalimat)

print(list(facebook))