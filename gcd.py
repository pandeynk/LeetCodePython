class GCDClass:
    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)


print(GCDClass.gcd(5, 10))
