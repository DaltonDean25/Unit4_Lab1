# Your Code & Heading go Here!
class ArrayStack:
  def __init__(self, stack=[], size=0):
    self.__stack = stack
    self.__size = size
  

  def push(self, element):
    """add a new element to top of stack"""
    self.__stack.append(element)


  def pop(self):
    """remove the element on the top of stack"""
    if not self.__is_empty():
      top = self.__stack[-1]
      self.__stack.remove(top)
      return top

    else:
      raise IndexError("List assignment index out of range")

  def top(self):
    """returns the element on the top of stack"""
    if not self.__is_empty():
      return self.__stack[-1]
    
    else:
      raise IndexError("List assignment index out of range")


  def __is_empty(self):
    """returns true if the stack is empty"""
    if len(self.__stack) == 0:
      return True
    
    return False
  
  
  def __len__(self):
    """returns the length of the stack"""
    return len(self.__stack)


  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out






