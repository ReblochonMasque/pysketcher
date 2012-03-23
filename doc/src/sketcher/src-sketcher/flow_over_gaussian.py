from pysketcher import *
from numpy import exp, linspace

W = 5    # upstream area
L = 10   # downstread area
H = 4    # height
sigma = 2
alpha = 2

drawing_tool.set_coordinate_system(xmin=0, xmax=W+L+1,
                                   ymin=-2, ymax=H+1,
                                   axis=True)
drawing_tool.set_linecolor('blue')

# Create bottom

def gaussian(x):
    return alpha*exp(-(x-W)**2/(0.5*sigma**2))

x = linspace(0, W+L)
y = gaussian(x)
wall = Wall(x, y, thickness=-0.3, pattern='|').set_linecolor('brown')

def velprofile(y):
    return [2*y*(2*H-y)/H**2, 0]

inlet_profile = VelocityProfile((0,0), H, velprofile, 5)
symmetry_line = Line((0,H), (W+L,H))
symmetry_line.set_linestyle('dashed')
outlet = Line((W+L,0), (W+L,H))
outlet.set_linestyle('dashed')

#print repr(inlet_profile)
fig = Compose({
    'bottom': wall,
    'inlet': inlet_profile,
    'symmetry line': symmetry_line,
    'outlet': outlet,
    })

fig.draw()  # send all figures to plotting backend

vx, vy = velprofile(H/2.)
symbols = {
    'alpha': DistanceSymbol((W,0), (W,alpha), r'$\alpha$'),
    'W': DistanceSymbol((0,-0.5), (W,-0.5), r'$W$',
                        symbol_spacing=-1./30),
    'L': DistanceSymbol((W,-0.5), (W+L,-0.5), r'$L$',
                        symbol_spacing=-1./30),
    'v(y)': Text('$v(y)$', (H/2., vx)),
    'dashed line': Line((W-2.5*sigma,0), (W+2.5*sigma,0)).set_linestyle('dotted').set_linecolor('black'),
    }
symbols = Compose(symbols)
symbols.draw()

drawing_tool.display()
drawing_tool.savefig('tmp1.png')


raw_input()
