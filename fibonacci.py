def fibonacci(numero):
  if numero == 1:
    return 0
  if numero == 2:
    return 1
  return fibonacci(numero - 1) + fibonacci(numero - 2)