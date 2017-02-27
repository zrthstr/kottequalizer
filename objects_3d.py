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


class Pyramid:
    ## a pyramind this time working with poligones
    hight_len = 3
    side_len = 2
    count = 0
    pyramid_id = 0
    offset = -3
    distance = 1


    def __init__(self):
        Pyramid.count += 1
        self.base_x = Pyramid.count * (self.side_len + self.distance)
        self.format()

        self.pyramid_id = Pyramid.pyramid_id
        Pyramid.pyramid_id += 1


    def __del__(self):
        Pyramid.count -= 1


    def format(self):
        self.right = self.base_x + self.side_len
        self.left = self.base_x
        self.back = self.side_len
        self.front = 0
        self.bottom = 0
        self.top = self.hight_len

        ###   [top, [lr][fb] ]
        self.c = {
                "top":[self.left + self.side_len / 2, self.top, self.side_len / 2],
                "lf" :[self.left,  self.bottom, self.front],
                "lb" :[self.left,  self.bottom, self.back],
                "rf" :[self.right, self.bottom, self.front],
                "rb" :[self.right, self.bottom, self.back],
                }

        return self.c


    def polygons(self):
        #return [[self.c["top"], self.c[k]] for k, v in self.c.items() if not k == "top"]
        return [
                [self.c["top"], self.c["lf"], self.c["rf"]],
                [self.c["top"], self.c["rf"], self.c["rb"]],
                [self.c["top"], self.c["rb"], self.c["lb"]],
                [self.c["top"], self.c["lb"], self.c["lf"]],
                ]

    def info(self):
        print("Pyramid: %d from: %d" % (self.pyramid_id, Pyramid.count))
        print("c=", self.c)



class Obj_loader:
    ### load and parse obj waveform file

    ### only the below data entries are implemented, there are some more, also see mtl files
    ### the blow section is straigt outta wikipedia
    ### https://en.wikipedia.org/wiki/Wavefront_.obj_file#File_format

    COMMENT = "#"

    # List of geometric vertices, with (x,y,z[,w]) coordinates, w is optional and defaults to 1.0.
    GEOMETRIC_VERTICES = "v"

    # List of texture coordinates, in (u, v [,w]) coordinates, these will vary between 0 and 1, w is optional and defaults to 0.
    TEXTURE_CORDIANTES = "vt"

    # List of vertex normals in (x,y,z) form; normals might not be unit vectors.
    VERTEX_NORMALS = "vn"

    # Parameter space vertices in ( u [,v] [,w] ) form; free form geometry statement ( see below )
    PARAMETER_VERTICES="vp"

    # Polygonal face element (exp.: f 1 2 3    or  f 3/1 4/2 5/3)
    POLYGONAL_FACE_ELEMENT = "f"


    def __init__(self, file_name, ignore_unknown_types=False):
        self.entrys = {
                GEOMETRIC_VERTICES:     [],
                TEXTURE_CORDIANTES:     [],
                VERTEX_NORMALS:         [],
                PARAMETER_VERTICES:     [],
                POLYGONAL_FACE_ELEMENT: []
            }


                }  ### dict of lists of entrys in obj waveform filefile 
        try:
            print("trying to load{0}".format(file_name))
            with open(file_name) as fd:
                for line in fd:
                    print("parsing line:", line, "< len:", len(line))

                    if len(line) == 1:
                        ### ignore empty lines..
                        continue
                    if line.strip()[0] == COMMENT:
                        ### ..and  comments 
                        continue

                    value = line.split()
                    if value[0] in self.entrys.keys():
                        ### known entry type!
                        parse_line(value)
                    elif ignore_unknown_types:
                        print("ignoring line:", line)
                        continue
                    else:
                        raise RuntimeError('Bad line found:' + line) from error

        except:
            print("failed to load file")
            raise
                            

        def parse_line(value):
            ### at this point we can savely make some asumtions about the line passed
            ### it is not a comment
            ### it is a known type of entry
            ### split() also ridded all double whitspaces and so on

            if value[0] == GEOMETRIC_VERTICES:
                if len(value) == 4:
                    value.append(1.0)
                if len(value) == 5:
                    self.entrys[GEOMETRIC_VERTICES].append([float(v) for v in value[1]])

            elif value[0] == TEXTURE_CORDIANTES:
                if len(value) == 3:
                    value.append(0.0) 
                if len(value) == 4:
                    self.entrys[TEXTURE_CORDIANTES].append([float(v) for v in value[1]])
                    for parameter in self.entrys[TEXTURE_CORDIANTES][-1]:
                        if 0 <= parameter <= 1:
                            raise RuntimeError("bad value in line" + str(value)) from error

            elif value[0] == POLYGONAL_FACE_ELEMENT:
                if 1 > len(value) > 5:
                    tmp = []
                    for v in value[1:]
                        if "/" in v:
                            raise RuntimeError("/// not inplemented yet")
                        if "." in v:
                            raise RuntimeError("Float not allowed i POLYGONAL_FACE_ELEMENT, found '.' character.")

                        tmp.append(int(v))
                    self.entrys[POLYGONAL_FACE_ELEMENT].append(tmp)

          else:
              raise RuntimeError("Unhandled type TBD!")



if __name__ == "__main__":
    main()

