train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

## Turn up the temperature

def f_to_c(fah):
  return (fah-32)*5/9

def c_to_f(cel):
  return cel*9/5+32

#test
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

## Use the force

def get_force(mass, acceleration):
  return mass*acceleration

def get_energy(mass, c=3*10**8):
  return mass*(c**2)

#test

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies %i N of force." % train_force)

bomb_energy = get_energy(bomb_mass)

print("A %i kg bomb supplies %i Joules of energy." % (bomb_mass, bomb_energy))

## Do the work

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration)*distance

#test
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does %i Joules of work over %i meters." % (train_work, train_distance))

