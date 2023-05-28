from abc import ABC, abstractmethod

def eval_polys(exp):
    operand, op, operand2 = exp
    match op:
        case '+':
            return Addition.compute(operand, operand2)
        case '-':
            return Subtraction.compute(operand, operand2)


class Polynomial(ABC):

    """
    Abstract class from which the leafs and the composite expression inherits
    from.
    """

    @abstractmethod
    def compute(self):
        pass


class Poly:
    """
    A polynomial POLY abstraction.
    """
    def __init__(self, *coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        return "Polynomial" + str(tuple(self.coefficients))

    def degree(self):
        return len(list(self.coefficients)) - 1


class Addition(Polynomial):
    """
    Main operation is COMPUTE: it adds two polynomials; the leaf of the tree
    representing the operation.
    """

    def compute(self, other):
        result_poly = [coeff + coeff2 for coeff, coeff2 in zip(list(self.coefficients), list(other.coefficients))]
        return Poly(*result_poly)

class Subtraction(Polynomial):
     """
    Main operation is COMPUTE: it subtracts two polynomials; the leaf of the 
    representing the operation.
    """
     def __init__(self, poly, poly2):
         self.poly = poly
         self.poly2 = poly2
         
     def compute(self):
         result_poly = [coeff - coeff2 for coeff, coeff2 in zip(list(self.poly.coefficients), list(self.poly2.coefficients))]
         return Poly(*result_poly)

class CompositeAddition(Polynomial):

    def __init__(self, *polynomials):
        self.polynomials = list(polynomials)

    def compute(self):
        coefficients = list()
        for poly in self.polynomials:
            coefficients.append(poly.coefficients)
        result = [s + t + z for s, t, z in zip(*coefficients)]
        return Poly(*result)


class CompositeSubtraction(Polynomial):
    
    def __init__(self, *polynomials):
        self.polynomials = list(polynomials)

    def compute(self):
        coefficients = list()
        for poly in self.polynomials:
            coefficients.append(poly.coefficients)

        result = [s - t - z for s, t, z in zip(*coefficients)]

        return Poly(*result)

class Integer:

    def __init__(self, integer):
        self.integer = integer

    def __repr__(self):
        return "Integer" + "(" + str(self.integer) + ")"

class Deriv(Polynomial):
    
    def __init__(self, poly):
        if not isinstance(poly, Poly):
            raise ValueError("{} is not of type Poly.".format(poly))
        else:
            self.poly = poly

    def compute(self):
        """
        Given a polynomial it computes the derivative.
        
        @param poly: a polynomial
        @returns: a polynomial, the derivative
        """
        coeffs = list()
        exponent = self.poly.degree()
        poly_coeffs = list(self.poly.coefficients)
        for i in range(len(poly_coeffs) - 1):
            coeffs.append(poly_coeffs[i] * exponent)
            exponent -= 1

        return Poly(*coeffs)


def eval_poly(poly, x):
    """
    given a polynomial and a value for x, solve the polynomial.
   
    @param: Poly
    @param: a variable x

    @returns: evaluation of polynomial given the value of x.
    """
    degree = poly.degree()
    solution = 0
    coefficients = list(poly.coefficients)
    for i in range(len(coefficients)):
        solution += (x ** degree) * coefficients[i]
        degree -= 1
        
    return Integer(solution)
                   
        
