import subprocess;
var = "ExifTool.jpg"
pipe = subprocess.Popen(["./exiftool", var], stdin=subprocess.PIPE)
result = pipe.stdout.read();
print result
fileobj = open(var+".txt", "r+");
fileobj.write(result);
fileobj.close();
pipe.stdin.close()
