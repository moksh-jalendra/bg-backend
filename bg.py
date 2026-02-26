from withoutbg import WithoutBG


def bg_remove(z):
    model = WithoutBG.opensource()
    resut = model.remove_background(z)
    resut.save('photo-withoutbg.png')
