def tower_of_hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 disks from source to auxiliary using target as the auxiliary rod
        tower_of_hanoi(n - 1, source, target, auxiliary)
        
        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")
        
        # Move n-1 disks from auxiliary to target using source as the auxiliary rod
        tower_of_hanoi(n - 1, auxiliary, source, target)

# Example usage:
num_of_disks = 3
tower_of_hanoi(num_of_disks, 'A', 'B', 'C')

