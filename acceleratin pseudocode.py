velocity = 0
acceleration_grounded = 5
soft_v_cap = 100
SCD = 1

while True:
    if velocity < soft_v_cap or SCD > 1:
        velocity += acceleration_grounded
    if velocity > soft_v_cap and SCD < 5:
        velocity -= SCD
    if SCD < 1:
        SCD = 1