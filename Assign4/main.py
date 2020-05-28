from shapes import *
from animals import *
from abc import *
import time

cat = Cat();    cat.describe()
lion = Lion();  lion.describe()
Tiger().describe()
SaberTooth().describe()
Canidae().describe()
Dog().describe()
Wolf().describe()
PolarBear().describe()
Monkey().describe()

print("Moving on to shapes")
time.sleep(0.5)

t.shape('arrow')
Square().draw();                t.reset();    t.speed(2);
Rhombus().draw();         t.reset();    t.speed(2);
Rectangle(200,100).draw();             t.reset();    t.speed(2);
Parallelogram(150 , 250).draw();         t.reset();    t.speed(2);
Circle().draw();                t.reset();    t.speed(2);  
Pentagon().draw() ;             t.reset();    t.speed(2);
Hexagon().draw();               t.reset();    t.speed(2);
Triangle(180, 240,300).draw();              t.reset();    t.speed(2);    
EquilateralTriangle().draw();   t.reset();    t.speed(2);
Cone().draw();                  t.reset();    t.speed(2);


