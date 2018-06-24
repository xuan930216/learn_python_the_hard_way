# Is a number prime?
# prime number is 6n + 1 or 6n - 1 except 2 and 3
def is_prime(num):
  if num <=1 :
      return False
  elif num == 2 or num == 3 :
      return True
  else:
      number_smaller = (num -1)%6
      number_larger = (num + 1)%6
      if number_larger == 0 or number_smaller == 0:
          return True
      else:
          return False
