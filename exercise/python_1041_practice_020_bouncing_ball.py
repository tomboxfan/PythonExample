'''
Requirement:
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

'''
思考过程:
During each bounce, total travel distance is composed of 2 parts:
1) drop
2) bounce

drop1 = 100
bounce1 = drop1 / 2

drop2 = bounce1
bounce2 = drop2 / 2

drop3 = bounce2
bounce3 = drop3 / 2

... ...

So the looping body is always:
drop = previous bounce
bounce = drop / 2
'''

init_height = 100

# because it asks total travel distance, so:
total_travel_distance = 0

bounce = 100

for bounce_time in range(10000):

    drop = bounce
    bounce = drop / 2
    print(f'Bouncing time: {bounce_time}. Travel to the ground: {drop:.4f}m, travel to the sky: {bounce:.4f}m.')

    total_travel_distance += drop
    total_travel_distance += bounce
    print(f'Total travel distance: {total_travel_distance:.4f}m.')


print(f'Now the ball is at height: {bounce:.4f}m.')