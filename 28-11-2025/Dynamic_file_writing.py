g_line= lambda user: f"Hello {user}! welcome to python"

def write_dynamic_content(user,filename):
    with open(filename,"w") as f:
        f.write(g_line(user))
write_dynamic_content("Bishal","notex.txt")
