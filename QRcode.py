pip install qrcode
import qrcode
img = qrcode.make('https://www.youtube.com/channel/UC6rM-nVyC284aXst43arWVw')
img.save('youtubeQR.jpg')