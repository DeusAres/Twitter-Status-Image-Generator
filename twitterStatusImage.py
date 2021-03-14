import manager, drawerFunctions
import textwrap
def drawTwitterStatus(profile_picture, username, name, message, date_time_twitter):
    
    profile_picture = drawerFunctions.openImage(profile_picture)
    profile_picture = drawerFunctions.resize(profile_picture, 80, 80)
    profile_picture = drawerFunctions.roundCorners(profile_picture, int(profile_picture.height/2))

    W, H = 1000, 500
    canvasB, canvasD = drawerFunctions.backgroundJPG(W, H, "#15202b")
    canvasB = drawerFunctions.pasteItem(canvasB, profile_picture, 24, 20)

    font_helvetica = #PATH TO HELVETICA
    font_helveitca_bold = #PATH TO HELVETICA BOLD

    font = drawerFunctions.fontDefiner(font_helvetica, 25)
    canvasD = drawerFunctions.drawText(125, 30, canvasD, name, "#ffffff", font)

    font = drawerFunctions.fontDefiner(font_helveitca_bold, 25)
    canvasD = drawerFunctions.drawText(125, 62, canvasD, username, "#8b9ca9", font)

    font = drawerFunctions.fontDefiner(font_helvetica, 35)
    width_size = 60
    message_wrapped = textwrap.wrap(message, width = width_size, break_long_words=True)

    while drawerFunctions.getSize(message_wrapped[0], font)[0] >= 900:
        width_size -= 1
        message_wrapped = textwrap.wrap(message, width = width_size, break_long_words=True)

    y = 135    
    for line in message_wrapped: 
        canvasD = drawerFunctions.drawText(24, y, canvasD, line, "#ffffff", font)
        y = y + drawerFunctions.getSize(line, font)[1] + 5

    y += 25

    font = drawerFunctions.fontDefiner(font_helvetica, 25)

    bottom_text = date_time_twitter[0] + " - " +  date_time_twitter[1] + " - " +  date_time_twitter[2]
    canvasD = drawerFunctions.drawText(24, y, canvasD, bottom_text, "#8b9ca9", font)

    y = y + drawerFunctions.getSize(bottom_text, font)[1] + 20

    canvasB = drawerFunctions.cropImage(canvasB, (0, 0, W, y))
    
    return canvasB


"""
message = "Lorem Ipsum"
username = "@LoremIpsum"
name = "Lorem Ipsum"
profile_picture = "C:\\Users\\User\\Desktop\\image.jpg"
date_time_twitter = ["13:40", "14 Mar 2021", "Twitter for iOS"]
drawTwitterStatus(profile_picture, username, name, message, date_time_twitter)
"""