import math

def colebrook_eq(Re, epsilon, f_guess=0.02, max_iter=1000, tol=1e-6):
    """
    Function to solve Colebrook equation for friction factor using iterative method.
    
    Args:
    - Re: Reynolds number
    - epsilon: relative roughness
    - f_guess: initial guess for friction factor (default: 0.02)
    - max_iter: maximum number of iterations (default: 1000)
    - tol: tolerance for convergence (default: 1e-6)
    
    Returns:
    - f: friction factor
    """
    f = f_guess
    for _ in range(max_iter):
        f_new = (-2 * math.log10((epsilon / 3.7) + (2.51 / (Re * math.sqrt(f)))))**-2
        if abs(f_new - f) < tol:
            return f_new
        f = f_new
    return None

def get_friction_factors(Re_list, epsilon):
    """
    Function to calculate friction factors for given Reynolds numbers using Colebrook equation.
    
    Args:
    - Re_list: list of Reynolds numbers
    - epsilon: relative roughness
    
    Returns:
    - friction_factors: dictionary containing Reynolds numbers as keys and corresponding friction factors as values
    """
    friction_factors = {}
    for Re in Re_list:
        friction_factors[Re] = colebrook_eq(Re, epsilon)
    return friction_factors

def check_blood_pressure(status):
    """
    Function to check the status of blood pressure.
    
    Args:
    - status: tuple containing systolic and diastolic blood pressure values
    
    Returns:
    - status_str: string indicating the status of blood pressure
    """
    systolic, diastolic = status
    if systolic < 90 or diastolic < 60:
        return "Low blood pressure"
    elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
        return "Ideal blood pressure"
    else:
        return "High blood pressure"

# Reynolds numbers and relative roughness
Re_list = [300, 600, 900, 3000, 6000, 9000]
epsilon = 0.000166

# Calculate friction factors
friction_factors = get_friction_factors(Re_list, epsilon)
print("Reynolds number (NRe)\tFriction factor (f)")
for Re, f in friction_factors.items():
    print(f"{Re}\t\t\t{f:.6f}")

# Blood pressure input
systolic = float(input("Enter systolic blood pressure (mmHg): "))
diastolic = float(input("Enter diastolic blood pressure (mmHg): "))

# Check blood pressure status
blood_pressure_status = check_blood_pressure((systolic, diastolic))
print("Blood pressure status:", blood_pressure_status)


