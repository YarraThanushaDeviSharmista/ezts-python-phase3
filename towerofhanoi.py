def tower(n,source,temp,destination):
    if n==1:
        print(f"move the 1 disk from {source} to {destination}")
        return
    tower(n-1,source,destination,temp)
    print(f"move the {n} disk from {source} to {destination}")
    tower(n-1,temp,source,destination)
tower(3,'A','B','C')
