#!/usr/bin/env python

def main():
    print(__name__)

    box1 = Box("green")
    print("lines::", box1.lines)


class Box:
    start = -5
    box_count = 0
    offset = 2 
    width = 1
    hight = 2
    depth = 1


    def __init__(self, color="default_color"):
        self.base = Box.box_count * (self.width + self.offset) + self.start
        self.color = color
        self.position = Box.box_count
        Box.box_count += 1
        self.formate()


    def formate(self):

        self.c = {
                "ldb" : [self.base,     0,          0],
                "ldf" : [self.base,     0,          1],
                "lub" : [self.base,     self.hight, 0],
                "luf" : [self.base,     self.hight, 1],
                "rdb" : [self.base + 1, 0,          0],
                "rdf" : [self.base + 1, 0,          1],
                "rub" : [self.base + 1, self.hight, 0],
                "ruf" : [self.base + 1, self.hight, 1]
                }


        ## [ l r ][ d u ][ b f ]
        self.lines = [
               [self.c["ldb"],self.c["ldf"]],
               [self.c["ldb"],self.c["lub"]],
               [self.c["ldb"],self.c["rdb"]],

               [self.c["ldf"],self.c["rdf"]],
               [self.c["ldf"],self.c["luf"]],
               
               [self.c["lub"],self.c["rub"]],
               [self.c["lub"],self.c["luf"]],
               
               [self.c["rdb"],self.c["rub"]],
               [self.c["rdb"],self.c["rdf"]],

               [self.c["ruf"],self.c["rdf"]],
               [self.c["ruf"],self.c["rub"]],
               [self.c["ruf"],self.c["luf"]],
                ]


    def resize(self, f_hight=1.0, f_width=1.0, f_depth=1.0):
        self.hight *= f_hight
        self.width *= f_width
        self.depth *= f_depth
        self.formate()


    def __del__(self):
        Box.box_count -= 1


    def info(self):
        print("offset:%s, color:%s" % (self.base, self.color))
        print("box %d from %d boxes" % (self.position, Box.box_count))
        print("self.c:", self.c)
        print("lines: ",self.lines)


class Pyramide:
    ## a pyramind this time working with poligones
    hight_len = 3
    side_len = 2
    count = 0
    offset = -3
    distance = 1

    def __init__(self):
        Pyramide.count += 1
        self.formate()
        this.base_x = Pyramide.count * (side_len + distance)

    def __del__(delf):
        Pyramide.count -= 1


    def format(self):
        this.right = this.base_x + this.side_len
        this.left = this.base_x
        this.back = side_len
        this.front = 0
        c={
                "top":[this.left + this.side_len / 2, hight_len / 2],
                "lf" :[this.left,  this.front],
                "lb" :[this.left,  this.back],
                "rf" :[this.right, this.front],
                "rb" :[this.right, this.back],
                }

        return c

    def polygons(self):
        return [[c["top"],c[e]] for k, v in c.items() if not k == "top"]



if __name__ == "__main__":
    main()

