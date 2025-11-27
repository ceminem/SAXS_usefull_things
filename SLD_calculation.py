#pipline for the calculation of the Scattering Length Density

#constants 
Na = 6.022e23 #1/mol
re = 2.282e-6 #nm
H_molmass = 1.01
C_molmass  = 12.01
O_molmass  = 16 

H_electrons = 1
C_electrons = 6
O_electrons = 8


density_input = input("Give me the density of the sample you of which you want to calculate the SLD: ")
density_float = float(density_input) * 10**-21 #converting g/cm3 in g/nm

H_input = input('Give me the amount of H-Atoms: ')
H_int = int(H_input)

C_input = input('Give me the amount of C-Atoms: ')
C_int = int(C_input)

O_input = input('Give me the amount of O-Atoms: ')
O_int = int(O_input)

molare_mass = H_int*H_molmass  + C_int*C_molmass  + O_int*O_molmass 
sum_of_scattering_events = H_int*H_electrons  + C_int*C_electrons  + O_int*O_electrons

sld = Na * re * density_float * sum_of_scattering_events/molare_mass
sld_unit_corrected = sld * 10**-4


print(f"The sld for your input is {sld_unit_corrected} x 10^-4 nm^-2")