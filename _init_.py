# define the color palette from Chinese traditional color, from book " 中国传统色- 故宫里的色彩美学"
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
class color_palette():

    def __init__(self) -> None:
        self.color_dict = defaultdict(list)
        pass

    def add_color(self, color_name, color_code):
        self.color_name = color_name
        self.color_code = color_code


    def RGB_list2hexString(self, list):
        hexString = '#'
        code = ''.join([np.base_repr(i, base=16) for i in list])
        #for i in list:
            #self.hexString += str(hex(i))[2:].zfill(2)
        return hexString+code

    def show_color_block(self, color_code):
        color = ''
        if isinstance(color_code, 'str'):
            if color_code[0] == '#':
                color = color_code
        if isinstance(color_code, 'list'):
            color = self.RGB_list2hexString(color_code)

        fig,ax = plt.subplots(figsize = (3,2))
        ax.add_patch(Rectangle((0,0), 1, 1, color=color))
        plt.show()