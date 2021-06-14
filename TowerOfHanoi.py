def solve_toh(n_disks):
    if n_disks == 0:
        return
    solve_toh(n_disks-1)
    move_disk(n_disks)
    solve_toh(n_disks-1)

def move_disk(n_disk):
    print("Move", str(n_disk))  

solve_toh(3)
