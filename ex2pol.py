def checkIntList(list):
    counter = 0
    for l in list:
        if str(type(l)) == "<class 'int'>":
            pass
        elif str(type(l)) == "<class 'float'>":
            pass
        else:
            counter += 1
    if counter == 0:
        return True
    else:
        return False


def checkIntDict(d):
    counter = 0
    for l, k in d.items():
        if str(type(l)) == "<class 'int'>" and str(type(k)) == "<class 'int'>":
            pass
        elif str(type(l)) == "<class 'int'>" and str(type(k)) == "<class 'float'>":
            pass
        elif str(type(l)) == "<class 'float'>" and str(type(k)) == "<class 'int'>":
            pass
        elif str(type(l)) == "<class 'float'>" and str(type(k)) == "<class 'float'>":
            pass
        else:
            counter += 1
    if counter == 0:
        return True
    else:
        return False


def convertIntDictIntoList(d: dict):
    for j, k in d.items():
        print(j, k)


def sgn(x):
    if x == 0:
        return 0
    else:
        sign = x / abs(x)
        return int(sign)


class CartesianPlane:
    def __init__(self, limx, limy, precision=1):
        self.limx = limx
        self.limy = limy
        self.precision = precision
        plane = list()
        n = limx
        while n >= -limx:
            m = limy
            while m >= -limy:
                plane.append([n, m])
                m -= precision

            n -= precision
        self.plane = plane
        xlist = list()
        ylist = list()
        for point in self.plane:
            xlist.append(point[0])
            ylist.append(point[1])
        self.xset = list(set(xlist))
        self.yset = list(set(ylist))
        self.graphedPoints = list()

    def __repr__(self):
        return self.plane

    def __str__(self):
        string = ""
        xset = self.xset
        yset = self.yset
        xset.sort()
        yset.sort()
        indexPoints = list()
        if len(self.graphedPoints) > 0:
            for element in self.graphedPoints:
                indexPoint = self.__repr__().index(element)
                indexPoints.append(indexPoint)
        indexX = [self.plane[i][0] for i in indexPoints]
        indexY = [self.plane[i][1] for i in indexPoints]

        for y in yset:
            if y in indexY:
                if indexY.count(y) == 1 and y == 0:
                    intIndex = indexY.index(y)
                    string += "\n"
                    for x in xset:
                        if x == indexX[intIndex]:
                            string += "X"
                        elif x == 0:
                            string += "|"
                        else:
                            string += "-"
                elif indexY.count(y) == 1 and y != 0:
                    intIndex = indexY.index(y)
                    string += "\n"
                    for x in xset:
                        if x == indexX[intIndex]:
                            string += "X"
                        elif x == 0:
                            string += "|"
                        else:
                            string += "o"
                elif indexY.count(y) > 1 and y != 0:
                    indexes = [i for i, var in enumerate(indexY) if var == y]
                    interestingX = [indexX[i] for i in indexes]
                    print(xset)
                    string += "\n"
                    for x in xset:
                        if x in interestingX:
                            string += "X"
                        elif x == 0:
                            string += "|"
                        else:
                            string += "o"
                elif indexY.count(y) > 1 and y == 0:
                    indexes = [i for i, var in enumerate(indexY) if var == y]
                    interestingX = [indexX[i] for i in indexes]
                    string += "\n"
                    for x in xset:
                        if x in interestingX:
                            string += "X"
                        elif x == 0:
                            string += "|"
                        else:
                            string += "-"

            elif y == 0:
                string += "\n-"
                for x in xset:
                    string += "-"
            else:
                string += "\n"
                for x in xset:
                    if x == 0:
                        string += "|"
                    else:
                        string += "o"

        return string

    def graph_point(self, point: list):
        x = point[0]
        y = - point[1]
        correspondentX = 1
        correspondentY = 1
        if abs(x) <= self.limx and abs(y) <= self.limy:
            for n in self.xset:
                distance = abs(x-n)
                if distance <= (self.precision/2):
                    correspondentX = n
                else:
                    pass
            for m in self.yset:
                distance = abs(y-m)
                if distance <= (self.precision/2):
                    correspondentY = m
                else:
                    pass
            correspondentPoint = [correspondentX, correspondentY]
            self.graphedPoints.append(correspondentPoint)
        else:
            pass


class PolynomialDict:
    def __init__(self, coefficients: dict):
        if checkIntDict(coefficients) == True:
            self.coefficientsDict = coefficients
        else:
            self.coefficientsDict = {0: 0}

    def __str__(self):
        string = ""
        for k, l in self.coefficientsDict.items():
            exponent = str(k)
            coefficient = str(abs(l))
            stringsegment = f"{coefficient}x^{exponent}"
            if exponent == "0":
                if sgn(l) == 1:
                    string = string + stringsegment
                else:
                    string = "-" + string + stringsegment
            else:
                if l >= 0:
                    string = string + " + " + stringsegment
                else:
                    string = string + " - " + stringsegment
        return string

    def deg(self):
        deegre = max(list(self.coefficientsDict.keys()))
        if self.coefficientsDict[deegre] == 0:
            newDict = self.coefficientsDict
            newDict.pop(deegre)
            newPol = PolynomialDict(newDict)
            return newPol.deg()
        else:
            return deegre

    def __repr__(self):
        string = ""
        for k, l in self.coefficientsDict.items():
            exponent = str(k)
            coefficient = str(abs(l))
            stringsegment = f"({coefficient})*(x**({exponent}))"
            if exponent == "0":
                if sgn(1) == 1:
                    string = string + stringsegment
                else:
                    string = "-" + string + stringsegment
            else:
                if l >= 0:
                    string = string + " + " + stringsegment
                else:
                    string = string + " - " + stringsegment
        return string

    def shownthcoefficient(self, n):
        if n in self.coefficientsDict.keys():
            return self.coefficientsDict[n]
        else:
            return 0

    def showList(self):
        return self.coefficientsDict

    def calculate(self, a):
        total = 0
        for k, i in self.coefficientsDict.items():
            exponent = k
            coefficient = i
            value = a ** exponent
            value2 = coefficient * value
            total += value2
        return total

    def __sub__(self, other):
        resultPol = dict()
        for k, i in self.coefficientsDict.items():
            if k in other.coefficientsDict.keys():
                newCoeff = self.coefficientsDict[k] - other.coefficientsDict[k]
                resultPol.update({k: newCoeff})
            else:
                resultPol.update({k: self.coefficientsDict[k]})
        for l in other.coefficientsDict.keys():
            if l not in self.coefficientsDict.keys():
                resultPol.update({l: other.coefficientsDict[l]})
            else:
                pass
        Result = PolynomialDict(resultPol)
        return Result

    def __mul__(self, other):
        tupleList = []
        newDict = dict()
        for k, i in self.coefficientsDict.items():
            coefficient = i
            exponent = k
            for j, l in other.coefficientsDict.items():
                coefficient2 = l
                exponent2 = j
                newcoeff = i * l
                newexponent = exponent + exponent2
                tuple = (newcoeff, newexponent)
                tupleList.append(tuple)
                if newexponent in newDict.keys():
                    newcoeff = newcoeff + newDict[newexponent]
                    newDict.update({newexponent: newcoeff})
                else:
                    newDict.update({newexponent: newcoeff})

        resultPolynomial = PolynomialDict(newDict)
        return resultPolynomial

    def __add__(self, other):
        factorpol = PolynomialDict({0: -1})
        newpol = factorpol * other
        resultPol = self - newpol
        return resultPol


class Polynomial:
    def __init__(self, coefficients: list):
        if checkIntList(coefficients) == True:
            self.coefficients = coefficients
        else:
            self.coefficients = [0]

    def shownthcoefficient(self, n):
        if n <= len(self.coefficients) - 1:
            return self.coefficients[n]
        else:
            return 0

    def deg(self):
        return len(self.coefficients) - 1

    def calculate(self, a):
        total = 0
        for k, i in enumerate(self.coefficients):
            exponent = k
            coefficient = i
            value = a ** exponent
            value2 = coefficient * value
            total += value2
        return total

    def showList(self):
        return self.coefficients

    def formTable(self, start, end, step):
        finalTable = dict()
        if str(type(step)) == "<class 'int'>":
            for n in range(start, end + 1, step):
                value = n
                polynomialValue = self.calculate(n)
                finalTable.update({value: polynomialValue})
        else:
            i = start
            while i <= end:
                value = i
                polynomialValue = self.calculate(i)
                finalTable.update({value: polynomialValue})
                i += step

        return finalTable

    def graph(self, plane: CartesianPlane):
        start = - plane.limx
        end = plane.limx
        step = plane.precision
        formedTable = self.formTable(start, end, step)
        codomain = list()
        print(formedTable)
        for l in formedTable.keys():
            codomain.append(formedTable[l])

        newlimy = plane.limy
        if newlimy > plane.limy:
            newlimy = max(codomain)

        newPlane = CartesianPlane(plane.limx, newlimy, plane.precision)

        for k, l in formedTable.items():
            pointToGraph = list()
            pointToGraph.append(k)
            pointToGraph.append(l)
            print(pointToGraph)
            newPlane.graph_point(pointToGraph)
        print(newPlane)

    # A more user-friendly representation.

    def __str__(self):
        string = ""
        for k, i in enumerate(self.coefficients):
            exponent = str(k)
            coefficient = str(abs(i))
            stringsegment = f"{coefficient}x^{exponent}"
            if exponent == "0":
                if sgn(i) == 1:
                    string = string + stringsegment
                else:
                    string = "-" + string + stringsegment
            else:
                if i >= 0:
                    string = string + " + " + stringsegment
                else:
                    string = string + " - " + stringsegment
        return string

    # If you assign a value to the variable x before, you can actually evaluate the expression returned by __repr__ method by using the eval() function.
    def __repr__(self):
        string = ""
        for k, i in enumerate(self.coefficients):
            exponent = str(k)
            coefficient = str(abs(i))
            stringsegment = f"({coefficient})*(x**{exponent})"
            if exponent == "0":
                string = string + stringsegment
            else:
                if i >= 0:
                    string = string + " + " + stringsegment
                else:
                    string = string + " - " + stringsegment
        return string

    def transform(self):
        polDict = dict()
        for k, i in enumerate(self.coefficients):
            polDict.update({k: i})
        newPol = PolynomialDict(polDict)
        return newPol

    # Polynomial Ring Algebra: addition, subtraction and multiplication

    def __add__(self, other):
        degree1 = len(self.coefficients) - 1
        degree2 = len(other.coefficients) - 1
        if degree1 == degree2:
            newpol = self.coefficients
            for k, i in enumerate(self.coefficients):
                newCoeff = self.coefficients[k] + other.coefficients[k]
                newpol[k] = newCoeff
            resultPol = Polynomial(newpol)
            return resultPol
        elif degree1 > degree2:
            newPol = self.coefficients
            for k, i in enumerate(other.coefficients):
                newCoeff = self.coefficients[k] + other.coefficients[k]
                newPol[k] = newCoeff
            resultPol = Polynomial(newPol)
            return resultPol
        elif degree1 < degree2:
            newPol = other.coefficients
            for k, i in enumerate(self.coefficients):
                newCoeff = self.coefficients[k] + other.coefficients[k]
                newPol[k] = newCoeff
            resultPol = Polynomial(newPol)
            return resultPol

    def __sub__(self, other):
        degree1 = len(self.coefficients) - 1
        degree2 = len(other.coefficients) - 1
        if degree1 == degree2:
            newpol = self.coefficients
            for k, i in enumerate(self.coefficients):
                newCoeff = self.coefficients[k] - other.coefficients[k]
                newpol[k] = newCoeff
            resultPol = Polynomial(newpol)
            return resultPol
        elif degree1 > degree2:
            newPol = self.coefficients
            for k, i in enumerate(other.coefficients):
                newCoeff = self.coefficients[k] - other.coefficients[k]
                newPol[k] = newCoeff
            resultPol = Polynomial(newPol)
            return resultPol
        elif degree1 < degree2:
            newPol = other.coefficients
            for k, i in enumerate(self.coefficients):
                newCoeff = self.coefficients[k] - other.coefficients[k]
                newPol[k] = newCoeff
            for j in range(degree1 + 1, degree2 + 1):
                newPol[j] = - newPol[j]
            resultPol = Polynomial(newPol)
            return resultPol

    def __mul__(self, other):
        tupleList = []
        newDict = dict()
        for k, i in enumerate(self.coefficients):
            for j, l in enumerate(other.coefficients):
                newcoeff = i * l
                newexponent = k + j
                tuple = (newcoeff, newexponent)
                tupleList.append(tuple)
                if newexponent in newDict.keys():
                    newcoeff = newcoeff + newDict[newexponent]
                    newDict.update({newexponent: newcoeff})
                else:
                    newDict.update({newexponent: newcoeff})
        resultPolynomial = PolynomialDict(newDict)
        return resultPolynomial

    # Canonical polynomial equivalence relation = (Principle of identity of polynomials)

    def __eq__(self, other):
        coeff1 = self.coefficients
        coeff2 = other.coefficients
        counter = 0
        if self.deg() == other.deg():
            for i, l in enumerate(coeff1):
                if coeff1[i] == coeff2[i]:
                    pass
                else:
                    counter += 1
        else:
            counter += 1
        if counter == 0:
            return True
        else:
            return False


# Quaternion Algebra: 4 dimensional unitary associative algebra over the reals.


class Quaternion:
    def __init__(self, real, ipart, jpart, kpart):
        self.realpart = real
        self.ipart = ipart
        self.jpart = jpart
        self.kpart = kpart
        self.vec = [ipart, jpart, kpart]

    def __repr__(self):
        return f"{self.realpart} + ({self.ipart})i + ({self.jpart})j + ({self.kpart})k"

    def __getitem__(self, key):
        if key == 0:
            return self.realpart
        elif key == 1:
            return self.ipart
        elif key == 2:
            return self.jpart
        elif key == 3:
            return self.kpart
        else:
            pass

    def __str__(self):
        string = f"{self.realpart} "
        stringiPart = f"{abs(self.ipart)}i "
        stringjPart = f"{abs(self.jpart)}j "
        stringkPart = f"{abs(self.kpart)}k "
        if self.ipart < 0:
            stringiPart = "- " + stringiPart
        else:
            stringiPart = "+ " + stringiPart
        if self.jpart < 0:
            stringjPart = "- " + stringjPart
        else:
            stringjPart = "+ " + stringjPart
        if self.kpart < 0:
            stringkPart = "- " + stringkPart
        else:
            stringkPart = "+ " + stringkPart
        stringFinal = string + stringiPart + stringjPart + stringkPart
        return stringFinal

    def conjugate(self):
        newipart, newjpart, newkpart = -self.ipart, -self.jpart, -self.kpart
        conjugate = Quaternion(self.realpart, newipart, newjpart, newkpart)
        return conjugate

    def magnitude(self):
        a, b, c, d = self.realpart, self.ipart, self.jpart, self.kpart
        magSquared = (a**2) + (b**2) + (c**2) + (d**2)
        mag = magSquared ** (1/2)
        return mag

    def inverse(self):
        scalar = 1 / ((self.magnitude()) ** 2)
        result = self.conjugate() * scalar
        return result

    def dot_product(self, other):
        a, b, c, d = self.realpart, self.ipart, self.jpart, self.kpart
        a2, b2, c2, d2 = other.realpart, other.ipart, other.jpart, other.kpart
        result = (a*a2) + (b*b2) + (c*c2) + (d*d2)
        return result

    def cross_product(self, other):
        a1, b1, c1, d1 = self.realpart, self.ipart, self.jpart, self.kpart
        a2, b2, c2, d2 = other.realpart, other.ipart, other.jpart, other.kpart
        if a1 == 0 and a2 == 0:
            iResult = (c1*d2) - (c2*d1)
            jResult = (b2*d1) - (b1*d2)
            kResult = (b1*c2) - (b2*c1)
            return Quaternion(0, iResult, jResult, kResult)
        else:
            return ""

    # Outer product of quaternions (p,q)
    def outer_product(self, other):
        a1, b1, c1, d1 = self.realpart, self.ipart, self.jpart, self.kpart
        a2, b2, c2, d2 = other.realpart, other.ipart, other.jpart, other.kpart
        vec1 = Quaternion(0, b1, c1, d1)
        vec2 = Quaternion(0, b2, c2, d2)
        result = (vec2*a1) - (vec1*a2) - (vec1.cross_product(vec2))
        return result

    def odd_product(self, other):
        a1, b1, c1, d1 = self.realpart, self.ipart, self.jpart, self.kpart
        a2, b2, c2, d2 = other.realpart, other.ipart, other.jpart, other.kpart
        vec1, vec2 = Quaternion(0, b1, c1, d1), Quaternion(0, b2, c2, d2)
        result = (Quaternion(a1*a2, 0, 0, 0)) - \
            (vec1*vec2) + (vec2*a1) + (vec1*a2)
        return result

    # Arithmetic operations in the H skew-field

    def __add__(self, other):
        totalreal = self.realpart + other.realpart
        totali = self.ipart + other.ipart
        totalj = self.jpart + other.jpart
        totalk = self.kpart + other.kpart
        result = Quaternion(totalreal, totali, totalj, totalk)
        return result

    def __sub__(self, other):
        result = self + Quaternion(-other.realpart, -
                                   other.ipart, -other.jpart, -other.kpart)
        return result

    # Multiplication (order matters)
    def __mul__(self, other):
        if str(type(other)) == "<class '__main__.Quaternion'>":
            a1, b1, c1, d1 = self.realpart, self.ipart, self.jpart, self.kpart
            a2, b2, c2, d2 = other.realpart, other.ipart, other.jpart, other.kpart
            realTotal = (a1*a2) - (b1*b2) - (c1*c2) - (d1*d2)
            iTotal = (a1*b2) + (b1*a2) + (c1*d2) - (d1*c2)
            jTotal = (a1*c2) - (b1*d2) + (c1*a2) + (d1*b2)
            kTotal = (a1*d2) + (b1*c2) - (c1*b2) + (d1*a2)
            result = Quaternion(realTotal, iTotal, jTotal, kTotal)
            return result
        elif str(type(other)) == "<class 'int'>":
            result = Quaternion(self.realpart * other, self.ipart *
                                other, self.jpart * other, self.kpart * other)
            return result
        elif str(type(other)) == "<class 'float'>":
            result = Quaternion(self.realpart * other, self.ipart *
                                other, self.jpart * other, self.kpart * other)
            return result

    def __truediv__(self, other):
        otherinverse = other.inverse()
        result = self * otherinverse
        return result

    def __eq__(self, other):
        list1 = [self.realpart, self.ipart, self.jpart, self.kpart]
        list2 = [other.realpart, other.ipart, other.jpart, other.kpart]
        counter = 0
        for i, l in enumerate(list1):
            if list1[i] == list2[i]:
                pass
            else:
                counter += 1
        if counter == 0:
            return True
        else:
            return False
