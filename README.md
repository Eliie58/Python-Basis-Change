# Python-Basis-Change
Change Basis of a vector in Python, and plot the results if possible

# Requirements
* Python 3.8
* Numpy
* MatplotLib

# Running the program

To run this program, run python main.py, or the notebook change_basis

# IO
The program will ask for:
1. Dimensions of the vector and basis
2. Old Basis
3. New Basis
4. The vector

The program will then print:
1. The vector in the canonical basis
2. The vector in the New basis

If the dimension is 2 or 3, the program will plot the results

# Samples

## 2D
Sample run :
![Alt text](images/Picture1.png?raw=true "2D Sample Run")

Plot :
![Alt text](images/Picture2.png?raw=true "2D Sample Plot")

Color Codes :
* Red : x axis
* Green : y axis
* Orange : Vector
* Light Gray : x component of the vector
* Dark Gray : y component of the vector

As can be seen on the right, the vector is equal to -0.3333 x axis units + 0.8883 y axis units, like the program output

## 3D
Sample run :
![Alt text](images/Picture4.png?raw=true "3D Sample Run")

Plot :
![Alt text](images/Picture3.png?raw=true "3D Sample Plot")

Color Codes :
* Red : x axis
* Green : y axis
* Blue : z axis
* Orange : Vector
* Light Gray : x component of the vector
* Dark Gray : y component of the vector
* Black : z component of the vector

As can be seen on the right, the vector is equal to 0.5 x axis units + 1 y axis units + 1 z axis units, like the program output