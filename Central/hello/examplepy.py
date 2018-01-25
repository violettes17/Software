def hellopy(event):
  print(event)

  name = event['data']
  if name == "":
    name = "World"

  return "Hello " + name + " from OVH Functions!"