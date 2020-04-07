def weight_on_planets():
   uw = float(input("What do you weigh on earth? "))
   mw = .38 * (uw)
   jw = 2.34 * (uw)
   print("\nOn Mars you would weigh", mw, "pounds.\nOn Jupiter you would weigh", jw, "pounds." )
   
   
   
if __name__ == '__main__':
   weight_on_planets()
