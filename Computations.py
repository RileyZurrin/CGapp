from fractions import Fraction
import numpy as np
import math
from kivy.uix.popup import Popup
from kivy.uix.label import Label



def p1(J,j1,j2):
    return ((2*J + 1)*math.factorial(J + j1 - j2)*math.factorial(J - j1 + j2)*math.factorial(j1 + j2 - J))/(math.factorial(j1 + j2 + J +1))

# second multipliers (top and bottom)
def ptop(J,M,j1,m1,j2,m2):
    return math.factorial(J + M)*math.factorial(J - M)*math.factorial(j1 - m1)*math.factorial(j1 + m1)*math.factorial(j2 - m2)*math.factorial(j2 + m2)

def pbot(J,j1,m1,j2,m2):
    try:
        return math.factorial(J + m1 + m2)*math.factorial(J - (m1+m2))*math.factorial(j1 - m1)*math.factorial(j1 + m1)*math.factorial(j2 - m2)*math.factorial(j2 + m2)
    except ValueError:
        return 0

# third multiplier
def summand(k,j1,j2,J,m1,m2):
    return ((-1)**k)/(math.factorial(k)*math.factorial(j1 + j2 - J - k)*math.factorial(j1 - m1 - k)*math.factorial(j2 + m2 - k)*math.factorial(J - j2 + m1 + k)*math.factorial(J - j1 - m2 + k))


def topCompute(J,M,j1,j2):
    CG = ""
    denominator = int(500000*J**3)
    for dm1 in range(int(-2 * j1), int(2 * (j1) + 1), 2):
        for dm2 in range(int(-2 * j2), int(2 * (j2) + 1), 2):
            if dm1 + dm2 == 2 * M:
                S = 0
                m1 = dm1 / 2
                m2 = dm2 / 2
                kmax1 = int(j1 + j2 - J)
                kmax2 = int(j1 - m1)
                kmax3 = int(j2 + m2)
                kmin1 = int(j2 - J - m1)
                kmin2 = int(j1 + m2 - J)
                for k in range(max(kmin1, kmin2, 0), min(kmax1, kmax2, kmax3) + 1):
                    S = S + summand(k, j1, j2, J, m1, m2)
                sign = np.sign(S)
                Coeff = p1(J, j1, j2) * ptop(J, M, j1, m1, j2, m2) * S ** 2
                if abs(1 - abs(Coeff)) > 1/denominator:
                    if sign == 1:
                        if CG == "":
                            CG = CG + str(Fraction(Coeff).limit_denominator(denominator)) + "|" + str(Fraction(j1)) + " " + str(Fraction(j2)) + " " + str(Fraction(m1)) + " " + str(Fraction(m2)) + "\u27E9"
                        else:
                            CG = CG + " " + "+" + " " + str(Fraction(Coeff).limit_denominator(denominator)) + "|" + str(Fraction(j1)) + " " + str(Fraction(j2)) + " " + str(Fraction(m1)) + " " + str(Fraction(m2)) + "\u27E9"
                    if sign == -1:
                        if CG == "":
                            CG = CG + "-" + " " + str(Fraction(Coeff).limit_denominator(denominator)) + "|" + str(Fraction(j1)) + " " + str(Fraction(j2)) + " " + str(Fraction(m1)) + " " + str(Fraction(m2)) + "\u27E9"
                        else:
                            CG = CG + " " + "-" + " " + str(Fraction(Coeff).limit_denominator(denominator)) + "|" + str(Fraction(j1)) + " " + str(Fraction(j2)) + " " + str(Fraction(m1)) + " " + str(Fraction(m2)) + "\u27E9"
                else:
                    if np.sign(Coeff) == 1:
                        CG = CG + "|" + str(Fraction(j1)) + " " + str(Fraction(j2)) + " " + str(Fraction(m1)) + " " + str(Fraction(m2)) + "\u27E9"
                    if np.sign(Coeff) == -1:
                        CG = CG + "-|" + str(Fraction(j1)) + " " + str(Fraction(j2)) + " " + str(Fraction(m1)) + " " + str(Fraction(m2)) + "\u27E9"
    return CG

def botCompute(j1,j2,m1,m2):
    CG = ""
    denominator = int(500000 * j1 ** 3)
    for dJ in range(int(2 * abs(j1 - j2)), int(2 * (j1 + j2)) + 1, 2):
        J = dJ / 2
        S = 0
        kmax1 = int(j1 + j2 - J)
        kmax2 = int(j1 - m1)
        kmax3 = int(j2 + m2)
        kmin1 = int(j2 - J - m1)
        kmin2 = int(j1 + m2 - J)
        for k in range(max(kmin1, kmin2, 0), min(kmax1, kmax2, kmax3) + 1):
            S = S + summand(k, j1, j2, J, m1, m2)
        sign = np.sign(S)
        Coeff = p1(J, j1, j2) * pbot(J, j1, m1, j2, m2) * S ** 2
        if abs(Coeff) != 1:
            if sign == 1:
                if CG == "":
                    CG = CG + str(Fraction(Coeff).limit_denominator(denominator)) + "|" + str(Fraction(J)) + " " + str(Fraction(m1 + m2)) + " " + str(Fraction(j1)) + " " + str(Fraction(j2)) + "\u27E9"
                else:
                    CG = CG + " " + "+" + " " + str(Fraction(Coeff).limit_denominator(denominator)) + "|" + str(Fraction(J)) + " " + str(Fraction(m1 + m2)) + " " + str(Fraction(j1)) + " " + str(Fraction(j2)) + "\u27E9"
            if sign == -1:
                if CG == "":
                    CG = CG + "-" + " " + str(Fraction(Coeff).limit_denominator(denominator)) + "|" + str(Fraction(J)) + " " + str(Fraction(m1 + m2)) + " " + str(Fraction(j1)) + " " + str(Fraction(j2)) + "\u27E9"
                else:
                    CG = CG + " " + "-" + " " + str(Fraction(Coeff).limit_denominator(denominator)) + "|" + str(Fraction(J)) + " " + str(Fraction(m1 + m2)) + " " + str(Fraction(j1)) + " " + str(Fraction(j2)) + "\u27E9"
        else:
            if Coeff == 1:
                CG = CG + "|" + str(Fraction(J)) + " " + str(Fraction(m1 + m2)) + " " + str(Fraction(j1)) + " " + str(Fraction(j2)) + "\u27E9"
            else:
                CG = CG + "-|" + str(Fraction(J)) + " " + str(Fraction(m1 + m2)) + " " + str(Fraction(j1)) + " " + str(Fraction(j2)) + "\u27E9"
    return CG


def properform(s):
    try:
       float(s)
    except ValueError:
        try:
            num, denom = s.split('/')
        except ValueError:
            return False
        else:
            return True
    else:
        return True


def convert(s):
    try:
        return float(s)
    except ValueError:
        num, denom = s.split('/')
        return float(num) / float(denom)

def topvalidity(a,b,c,d):
    CD = np.arange(abs(convert(c) - convert(d)),convert(c) + convert(d) + 1)
    A = np.arange(-convert(a), convert(a) + 1)
    if convert(a) in CD:
        if convert(b) in A:
            return True
        else:
            invalidtop1()
    else:
        invalidtop2()

def botvalidity(a,b,c,d):
    A = np.arange(-convert(a),convert(a) + 1)
    B = np.arange(-convert(b), convert(b) + 1)
    if convert(a) >= 0:
        if convert(b) >= 0:
            if convert(c) in A:
                if convert(d) in B:
                    return True
                else:
                    invalidbot1()
            else:
                invalidbot2()
        else:
            invalidbot3()
    else:
        invalidbot4()


def topcheck(a,b,c,d):
    if properform(a) and properform(b) and properform(c) and properform(d):
        if (convert(a) % (1 / 2)) == 0 and (convert(b) % (1 / 2)) == 0 and (convert(c) % (1 / 2)) == 0 and (convert(d) % (1 / 2)) == 0:
            if topvalidity(a,b,c,d):
                return True
        else:
            invalid()
    else:
        invalid()

def botcheck(a,b,c,d):
    if properform(a) and properform(b) and properform(c) and properform(d):
        if (convert(a) % (1 / 2)) == 0 and (convert(b) % (1 / 2)) == 0 and (convert(c) % (1 / 2)) == 0 and (convert(d) % (1 / 2)) == 0:
            if botvalidity(a,b,c,d):
                return True
        else:
            invalid()
    else:
        invalid()

# class MyPopup(Popup):
#     bg_color = ListProperty([0,0,0,1])

class MyLabel(Label):
    pass

def invalidtop1():
    toppop1 = Popup(title = 'Invalid Input', size_hint = (.8, .4), content = MyLabel(text = 'Must have J = |j1 - j2|, |j1 - j2| + 1, ..., j1 + j2.'))

    toppop1.open()

def invalidtop2():
    toppop2 = Popup(title = 'Invalid Input', size_hint = (.8, .4), content = MyLabel(text = 'Must have J = |j1 - j2|, |j1 - j2| + 1, ..., j1 + j2.'))

    toppop2.open()


def invalidbot1():
    botpop1 = Popup(title = 'Invalid Input', size_hint = (.8, .4), content = MyLabel(text = 'Must have m2 = -j2, -j2 + 1, ... , j2 - 1, j2.'))

    botpop1.open()

def invalidbot2():
    botpop2 = Popup(title = 'Invalid Input', size_hint = (.8, .4), content = MyLabel(text = 'Must have m1 = -j1, -j1 + 1, ... , j1 - 1, j1.'))

    botpop2.open()


def invalidbot3():
    botpop3 = Popup(title = 'Invalid Input', size_hint = (.8, .4), content = MyLabel(text='Must have j2 >= 0.'))

    botpop3.open()


def invalidbot4():
    botpop4 = Popup(title = 'Invalid Input', size_hint = (.8, .4), content = MyLabel(text='Must have j1 >= 0.'))

    botpop4.open()

def invalid():
    pop = Popup(title = 'Invalid Input', size_hint = (.8, .4), content = MyLabel(text='Each entry must either be an integer or a half integer.'))

    pop.open()

def invalid2():
    pop2 = Popup(title = 'Invalid Input', size_hint = (.8, .4), content = MyLabel(text = 'Inputs are too large.'))

    pop2.open()



