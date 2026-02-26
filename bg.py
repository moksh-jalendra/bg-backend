from withoutbg import WithoutBG
model = WithoutBG.opensource()

def bg_remove(z):
    resut = model.remove_background(z)
    resut.save('photo-withoutbg.png')
