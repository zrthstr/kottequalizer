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

        #self.lines = [[a,b] for _, a in self.c.items() for _, b in self.c.items() if not a == b]
        #self.lines = [x for x in self.lines if int(bool(x[0][0]) ^ bool(x[1][0])) + int(bool(x[0][1]) ^ bool(x[1][1])) + int(bool(x[0][2]) ^ bool(x[1][2])) == 1 ]
        #for c, line in enumerate(self.lines):
        #    if [line[1], line[0]] in self.lines:
        #        del self.lines[c]


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
        
        #print("old self.hight:", self.hight)
        #print("old self.width:", self.width)
        #print("old self.depth:", self.depth)

        self.hight *= f_hight
        self.width *= f_width
        self.depth *= f_depth
        
        #print("new self.hight:", self.hight)
        #print("new self.width:", self.width)
        #print("old self.depth:", self.depth)
       
        self.formate()


    def __del__(self):
        Box.box_count -= 1

    def info(self):
        print("offset:%s, color:%s" % (self.base, self.color))
        print("box %d from %d boxes" % (self.position, Box.box_count))
        print("self.c:", self.c)
        print("lines: ",self.lines)


if __name__ == "__main__":
    main()

