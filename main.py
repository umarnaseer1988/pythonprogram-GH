def greet(name):
  """
  This function greets a person by name.

  Args:
    name: The name of the person to greet.

  Returns:
    A greeting message.
  """
  return "Hello, " + name + "!"

if __name__ == "__main__":
  name = input("Enter your name: ")
  print(greet(name))
  
  import module
  print(module.get_name())
  print(module.get_number())