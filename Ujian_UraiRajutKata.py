class uraiRajutkata:
    def urai(self, urai):
        x = ''
        for i in range(len(urai)+1):
            x += urai[0:i]
        return x
    def rajut(self, rajut):
        z = set(rajut)
        y = ''
        y = rajut[-(len(z)+1):]
        print(z)
        return y

x = uraiRajutkata()
print(x.urai('Code'))
print(x.urai('Python'))
print(x.urai('Purwadhika'))
print(x.rajut('CCoCodCode'))
print(x.rajut('PPyPytPythPythoPython'))
print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))





