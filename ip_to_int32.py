def ip_to_int32(ip):
  # your code here
  arr = ip.split('.')
  return int(arr[0])*256**3+int(arr[1])*256**2+int(arr[2])*256+int(arr[3])