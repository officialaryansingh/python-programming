# a= 2.01
# int(a)
# print(int(a))

# a = float(input("enter num1: "))
# b = float(input("enter num2: "))
# print([(a+b),(a%b),(a!=b)])


# power of a number
# # a= float(input("Number :"))

# # n = float(input(f"power of number {int(a)} :"))

# # print(f"{int(a)}^{int(n)} is :", a**n)
# # # new world

# import pyttsx3
# e = pyttsx3.init()
# e.say("hello, No ..  One  !!!?????")
# e.runAndWait()

# Lists

# a =[1,3,54,6,2,32,12]
# a.sort()

# print(a)
# a.reverse()
# a.insert(2,45)
# # it is a command to in put 45 the index 2
# # means in place of 12 there will be 45

# print(a)

# a.sort()
# print(a)

# a.remove(12)
# print("12 is removed",a)
# a.append(6)
# print("when 67 is apended:",a )

# a.pop(3)
# print(a.pop(3))
# print(a)
# a.sort()
# print(a)
# a.append(True)

# a.append(1.25)
# a.append("Aryan")
# print(a)
# # .sort() is not applicable
# a.remove("Aryan") 
# a.remove(1)
# a.sort()
# print(a) # this give error as str, is also present in  the string , therefore in that case

# b = True 
# print(int(b)) # value of true :1


# a = (1,2,3,4,5.5,4)
# # methods
# print(a.index(5.5))
# print(a.count(4))
# # operations (but not methods)
# print(a[:5])




# new methods in set
# a = {1,2,4,6,5,3,"aryan",34,54,5,6,6}
# b = {8,11}
# print(a.union(b))


# digging into iteration
#  we can do iteraton of any of :
# list,tuple,dictonary,set,string
# by using basic steps
# 1. a = "",[],{},(),{keys:values}
# 2. for item in a:
# 3.   print(item)
# and its done



# talking about new fuction :"sum()"

# a = [1,2,3,False]
# print(sum(a),"sum of a")

# b = {1,2,3,False}
# print(sum(b))

# c = (1,2,3,True)
# print(sum(c))

# d = {1:10,2:20,3:30,4:False}
# print(sum(d)) #This will give only sum of keys and only if number or a boolean

# # Hence, sum function works in case of all : list,tuple,dictionary,set

# CHAPTER - 6 : Conditional Expressions

# a = int(input("Enter your age : ",))
# b = input("Enter your gender : ",)

# if (45>a>18 and b=="male"):
#     print("You can buy a race car.")
# elif(a==18 and b == "male"):
#     print("go to college and get a great job to earn money.")
# elif(12<a and b == "male"):
#     print("try to learn many things and study hard.")
# elif(a<12 and b == "male"):
#     print("eat properly and play a lot.")
# elif(a<0 and b == "female"):
#     print("your age is just like your IQ level")
#     print(" go to hell.")
# elif(a<0 and b == "male"):
#     print("Entered age is invalid")
# else:
#     print("Frankly.......\n\n\n\n\n\n\n\nI don't care!\n ask someone else.")                        


# a = int(input("Enter no. :",))
# if(a%2 == 0):
#     print("no. is even")

# if(a>= 20):
#     print("you can do it!")
# elif(0<a<20):
#     print("keep it up")
# elif(a<0):
#     print("invalide age")
# else:
#     print("bye bye")
# n = input()
# m = int(n)
# print(m) # i.e. we can not change float into int data type but 
#         # we can do typecasting of int into float 

"""

# chapter 8: recursion
n = 5
def sum(n):
    if((n-1) >= 0):
        return n + sum(n-1)
    elif(n == 1):
        return 1
    elif(n<0):
        return "invalide input"
    
sumation = sum(n)
print(sumation)

"""



# TUPLE 
# a,b,c = (1,2,3) # This is correct method of tuple unpacking 
# but ,
# a,b,c = (1,2,3,4,7) # this will return ValueError:too many values to unpack
# conteration of tuple

"""
a = (1,2,3)
b = (3,2,567)
c = a+b
print(c)
print("printing a + b: ", a+b)
"""

"""Hence in case of Tuples we can have repetead value in newly formed tuples"""

# map() fuction:

'''

num = [9,8,7,6]
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
squaresum = map(lambda x : x**2,numbers+num)
print(list(squares))  # [1, 4, 9, 16]
print(list(squaresum))#[1, 4, 9, 16, 81, 64, 49, 36]
'''

# ch-11-PS.>
# Q1.> Create a class Employee and add salary and increment
#      properties to it.
#      Write a method salaryAfterIncrement with a @property 
#       decorator with a setter which changes the value of
#       increment based on the salary.

"""
Solution.>

class Employee:
    salary = 1200000
    increment = 10 # 10%

    @property
    def salaryAfterIncrement(self):
        return self.salary * (1 + (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100 
    
e = Employee()
e.salaryAfterIncrement = 1300000
print(e.salary)
print(e.increment,"%")
print(e.salaryAfterIncrement)
 
"""
def nanomatintro():
    import pyttsx3
    engine = pyttsx3.init()
    pyttsx3.speak("""Nanoscience and Nanotechnology:

Nanoscience is defined as the study of the fundamental particles of molecules
and Nanostructures with at least one dimension roughly between 1 mm -100
mm .Nanoscience is a new way of creating novel chemical and biological
Nanostructures, understanding their properties and finally learning about how
to organize these new Nanostructures into larger and more Complex
functional structure and devices.
Objectives and aims of Nanoscience:
Nanoscience is the study and research of internal and external constraints
towards a fundamental Nanomaterials design strategy to impact processes
and device Technologies at Nanoscale. Inter and inter molecular constraints
are studied in internal constraints. Inter facial and dimensional constraints are
studied in external constraints. The constraints can be entropic, enthalpic,
organisational, mobility, transitions or relaxations.
                  Nanotechnology:
What is nanotechnology?
Nanotechnology is the manipulation of matter on a near-atomic scale to produce new
structures, materials and devices. The technology promises scientific advancement in many
sectors such as medicine, consumer products, energy, materials, and manufacturing.
Nano Technology can be defined as the application of Science and scientific
knowledge at the nano scale for industrial or commercial objective.

CLASSIFICATION:

Depending on the number of dimensions in the nanorange, materials can be
classified as follows:
(i) Zero-dimensional Nanomaterials: Here, all dimensions (x, y, z) are at
Nanoscale, i.e., no dimensions is greater than 100 nm. It includes
nanospheres and nanoclusters.
(ii) One-dimensional Nanomaterials: Here, two dimensions (x, y) are at
Nanoscale and the other is outside the Nanoscale. This leads to needle
shaped Nanomaterials. It includes nanofibres, nanotubes, nanorods, and
nanowires.
(iii) Two-dimensional Nanomaterials: Here, one dimension (x) is at Nanoscale
and the other two are outside the Nanoscale. The 2D Nanomaterials exhibit
plate-like shapes. It includes nanofilms, nanolayers and nanocoatings with
nanometre thickness.
(iv) Three-dimensional Nanomaterials: These are the Nanomaterials that are
not confined to the Nanoscale in any dimension. These materials have three
arbitrary dimensions above 100 nm. The bulks (3D) Nanomaterials are
composed of a multiple arrangement of nanosize crystals in different
orientations. It includes dispersions of nanoparticles, bundles of nanowires
and nanotubes as well as multi-nanolayers (polycrystals) in which the 0D, 1D
and 2D structural elements are in close contact with each other and form
interfaces. For the better understanding, Nanomaterials are again organized
into four types as follows.
(1) inorganic-based nanomaterials; (2) carbon-based nanomaterials; (3)
organic-based nanomaterials; and (4) composite-based nanomaterials.

(i) Carbon based nanomaterials
(ii) Metal based materials
(iii) Dendrimers
(iv) Composites

(i) Carbon based materials: These are composed of carbon, taking the form of
hollow spheres, ellipsoids or tubes. The spherical and ellipsoidal forms are
referred as fullerenes, while cylindrical forms are called nanotubes.
(ii) Metal based materials: These include quantum dots, nanogold, nanosilver
and metal oxides like TiO 2 . A quantum dot is a closely packed semiconductor
crystal comprised of hundreds or thousands of atoms, whose size is on the
order of a few nanometers to a few hundred.
(iii) Dendrimers: Dendrimers are repetitively branched molecules. The name
comes from the Greek word ‘dendron’ (tree). These Nanomaterials are
nanosize polymers built from branched units. The surface of a dendrimer has
numerous chain ends, which can perform specific chemical functions.
Dendrimers are used in molecular recognition, nanosensing, light harvesting.
They may be useful for drug delivery.
(iv) Composites: Composites are combination of nanoparticles with other
Nanoparticles or with larger, bulk-type materials. Nanoparticles like nanosize
Clays are added to products (auto parts, packaging materials, etc.) to
enhance mechanical, thermal, and flame-retardant properties.""")
    engine.runAndWait()



def nanoQutmcofni():
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("""The Quantum Confinement Effect

Quantum confinement effects describe electrons in terms of energy levels, potential
wells, valence bands, conduction bands, and electron energy band gaps.The quantum confinement effect is observed when the size of the particle is too small to
be comparable to the wavelength of the electron.

The properties of any material are essentially just the average of the quantum
effects acting on those atoms. As the particle size is shrunk – eventually reaching
nanosize – this averaging no longer works to describe the material’s physical
properties, and we must look at each individual atom’s quantum behavior – and their
interactions with one another – instead. This effect (also known as the quantum size
effect) is due to a phenomenon known as confinement and is more prevalent in
nanoparticles of 10 nm or less. It is well-known that particles can be described as
acting like a wave or a particle.

In a bulk material, the electrons are generally treated as wave-like and are “free” to
move between atoms. As we shrink the size of a particle, the spatial extent of
electron wave-function is comparable to the particle’s size, and the electron begins
to “feel” the presence of particle boundaries and adjust their energy accordingly. In
this way, electrons are now “confined” in quantized energy levels and the once
freely-moving electrons are now restricted into these specific levels.

Materials suddenly exhibit very different properties: opaque substances such as
copper become transparent; stable materials such as aluminum turn out to be
combustible; solids like gold become liquid at room temperature; and insulators such
as silicon become conductors.""")
    engine.runAndWait()

def Quantumdots():
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("""Quantum Dots

A powerful and fascinating result of quantum effects on the nanoscale is the concept
of ‘tunability’. By changing particle size, one can fine-tune a material’s property of
interest - such as changing the fluorescence color - which can then be used to
identify particles and label them with markers for various purposes.

Quantum dots are one of the most significant developments which exploit such
quantum tunability. They are nanoparticles less than 10 nm in size, made of
semiconductor materials that have fluorescent properties. Their properties are
closely related to their size and shape, and they lie between those of bulk
semiconductors and discrete molecules.

The Mechanics of Quantum Dots

Due to the quantization of the electrons’ energy, the dots can be easily manipulated
to fluoresce at predefined wavelengths. When incident light is shone on
semiconductor material, electrons are excited to a higher state and leave behind a
‘hole’. The excited electron and subsequent hole exist in a bound state – known as
an exciton – attracted to one another by the electrostatic Coulomb force. After a
certain (usually exceptionally short) length of time, the electron returns to its ground
state, emitting energy as a photon – a particle of light. This is the principle of
fluorescence.

The emitted photon’s energy is determined by the band gap energy between the
highest occupied and lowest unoccupied energy levels, the confinement energies of
the hole and the excited electron, and the bound energy of the exciton. Quantum
dots – bound by the quantum confinement effect – are highly manipulable and, assuch, they can be fine-tuned to exact fluorescing wavelengths. Quantum dots are up
to a thousand times brighter and glow longer than conventional fluorescent dyes.

Smaller dots have a greater band gap and, ultimately, absorb and emit at higher
wavelengths, with their light being bluer. Conversely, larger dots have a lower energy
gap and absorb and emit towards the redder end of the spectrum. Size plays an
important role in the synthesis of quantum dots: smaller dots suffer the effects of the
quantum realm more readily and, as such, are more tuneable. Larger dots have an
extended lifetime due to their shortened bandgap.

To improve the fluorescence quantum yield – essentially the “return rate” of
fluorescing photons – it is possible to add a shell to a quantum dot, usually
composed of a larger bandgap semiconductor material. This is thought to reduce the
access of electron-hole pairs to alternative recombination pathways and improves
the overall yield.

Quantum Dots in Quantum Computing

Such dots are promising for the development of solid-state quantum computers. A
“qubit” is the basic unit of quantum information, equivalent to a classical bit in our
modern binary systems. Quantum properties such as “spin” and “charge” can be
seen as qubits, and exploited in quantum computing. Contrary to a classical system
– qubits can exist in both states at once, instead of just one or the other.

Quantum dots are being investigated as “housing units” for subatomic particles such
as electrons - which have inherent spin, charge and other quantum properties – to
be used as qubits. These quantum dots can be placed in arrays, connected to
outside electronics for control and reading of the qubit states.""")
    engine.runAndWait()

#1. nanomatintro()
#2. nanoQutmconfi()