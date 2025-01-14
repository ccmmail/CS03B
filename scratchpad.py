def demo_kwargs(**kwargs):
   print ( type(kwargs) )
   for arg in kwargs:
      print ( "  ", arg )
   print()

def main():
   demo_kwargs(a = 2, b = 3, dog = "wag", cat = "meow",
               wolf = [4.5, "growl"])
   demo_kwargs(x = 1, y = "two")
   demo_kwargs()

if __name__ == "__main__":
   main()