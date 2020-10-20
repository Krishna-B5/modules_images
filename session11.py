from PIL import Image
import argparse


def j2p():
    img = Image.open('./images/1.jpg').convert('RGB')
    img.save('./images/111.png', 'png')

def p2j():
    img = Image.open('./images/1.png').convert('RGB')
    img.save('./images/111.jpg', 'jpeg')

def image_resizer(new_width=None, new_height=None):
    img = Image.open('./images/1.jpg')
    w,h = img.size
    print(w,h)
    if new_width:
        wpercent = (new_width/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((new_width,hsize), Image.ANTIALIAS)
        img.save('./images/1_resize_w.jpg')
    elif new_height:
        hpercent = (new_height/float(img.size[0]))
        wsize = int((float(img.size[1])*float(hpercent)))
        img = img.resize((new_height,wsize), Image.ANTIALIAS)
        img.save('./images/1_resize_h.jpg')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    # parser.add_argument('conversion', 
    #                     type=str,
    #                     help='convert jpg to png.')
    parser.add_argument('--res_w', 
                        type=int,
                        help='new width value.')
    parser.add_argument('--res_h', 
                        type=int,
                        help='new height value.')
    args = parser.parse_args()
    for k, v in args.__dict__.items():
        if k == 'j2p':
            j2p()
        elif k == 'p2j':
            p2j()
        elif k == 'res_w':
            image_resizer(new_width=v)
        elif k == 'res_h':
            image_resizer(new_height=v)
    