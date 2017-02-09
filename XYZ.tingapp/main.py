import tingbot
from tingbot import *

import vertex
from vertex import *

import edge
from edge import *

import camera
from camera import *

debug = False

# Let's store vertices and edges
vertices = []
edges = []

# Cube size
size = 100

# Register Camera
camera = Camera(500)
camera.rotateDirection()


# Let's create the 8 vertices of a cube
for x in xrange(2):
    for y in xrange(2):
        for z in xrange(2):
            vertices.append(
                Vertex(
                    (screen.width-size)/2 + x * size,
                    (screen.height-size)/2 + y * size,
                    z * size,
                    6
                )
            )
            
# Let's create the 4 edges of the front face of the cube
# First we can store the vertices that forms the front face of the cube
faceVertices = []
for v in vertices:
    if v.coordinates.z == 0:
        faceVertices.append(v)
# Then we can create the edge between the vertices of the front face
faceEdges = []
for v1 in faceVertices:
    for v2 in faceVertices:
        if v1 <> v2 and not(v1.coordinates.x <> v2.coordinates.x and v1.coordinates.y <> v2.coordinates.y): # the two vertices are different and are not forming a diagonal
            t1 = [v1,v2] in [[e.start, e.end] for e in faceEdges]
            t2 = [v2,v1] in [[e.start, e.end] for e in faceEdges]
            if not(t1 or t2): # This edges hasn't been created before.
                faceEdges.append(Edge(v1, v2, 2))
                
# Let's create all the edges of the cube (It should be 4 * 3 = 12 edges)
for v1 in vertices:
    for v2 in vertices:
        if v1 <> v2:
            X = v1.coordinates.x == v2.coordinates.x
            Y = v1.coordinates.y == v2.coordinates.y
            Z = v1.coordinates.z == v2.coordinates.z
            if X + Y + Z == 2: # Exactly two shared coordinates (same plane, no diagonal)
                t1 = [v1,v2] in [[e.start, e.end] for e in edges]
                t2 = [v2,v1] in [[e.start, e.end] for e in edges]
                if not(t1 or t2): # This edges hasn't been created before.
                    edges.append(Edge(v1, v2, 2))

@right_button.press
def toggleDebug():
    global camera
    camera.rotateZ(10)
    camera.rotateDirection()

@midright_button.press
def rotateCamera():
    global debug
    debug = not(debug)

@every(seconds=1.0/30)
def loop():
    global debug
    # drawing code here
    screen.fill(color='black')
    screen.text('X-Y-Z', xy = (screen.width/2,0), align = 'top')
    screen.text(str(len(faceVertices)) + " Vertices (front face)", xy = (0,screen.height-20), align = 'bottomleft', font_size = 15, color = 'white')
    screen.text(str(len(vertices)) + " Vertices", xy = (0,screen.height), align = 'bottomleft', font_size = 15, color = 'white')
    screen.text(str(len(faceEdges)) + " Edges (front face)", xy = (screen.width,screen.height-20), align = 'bottomright', font_size = 15)
    screen.text(str(len(edges)) + " Edges", xy = (screen.width,screen.height), align = 'bottomright', font_size = 15) # currently doubled 
    for fei,faceEdge in enumerate(faceEdges):
        faceEdge.plot()
        if debug:
            faceEdge.plotDebug(fei)
    for fvi, vertice in enumerate(faceVertices):
        vertice.plot()
        if debug:
            vertice.plotDebug(fvi)

    for i, vertice in enumerate(vertices):
        screen.text(
            str(i) + " : " + str(vertice.coordinates.info()),
            xy = (0, i * 15),
            align='topleft',
            font_size = 10,
            color = 'white'
        )

    for i, edge in enumerate(edges):
        screen.text(
            str(i) + " : " + str(vertices.index(edge.start)) + " -> " + str(vertices.index(edge.end)),
            xy = (screen.width, i * 15),
            align='topright',
            font_size = 10,
        )

    screen.text('Front View', font_size = 10)
    screen.text(
        'Camera Position: ',
        xy = (0, 150),
        align = 'left',
        font_size = 10)
    screen.text(
        '[' + str(round(camera.pos.x,2)) + ', ' + str(round(camera.pos.y,2)) + ', ' + str(round(camera.pos.z,2)) +']',
        xy = (0, 162),
        align = 'left',
        font_size = 10)
    screen.text(
        'Camera Direction: ',
        xy = (0, 180),
        align = 'left',
        font_size = 10)
    screen.text(
        '[' + str(round(camera.dir.x,2)) + ', ' + str(round(camera.dir.y,2)) + ', ' + str(round(camera.dir.z,2)) +']',
        xy = (0, 192),
        align = 'left',
        font_size = 10)

tingbot.run()
