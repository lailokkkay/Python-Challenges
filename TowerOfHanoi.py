def solve_toh(n_disks, source, mid, target):
    if n_disks == 1:
        return print("move disk",n_disks, "from", source, "to", target)
    solve_toh(n_disks-1, source, target, mid)
    print("move disk",n_disks, "from", source, "to", target)
    solve_toh(n_disks-1, mid, source, target)
solve_toh(3, 'A', 'B', 'C')
