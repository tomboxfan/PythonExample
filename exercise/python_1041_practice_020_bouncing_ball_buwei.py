'''
思考过程:
the total distance travelled is composed of a series of small distances.
If the ball bounces 100 times, it should contains 200 small distances.
So, all I need to do:
1) calculate and put these 200 small distances into a list
2) use python built-in function sum() to calculate the total distance
'''



def ball(init_height):
    list_of_height=[]
    number_of_bounces = int(input("How many times it bounced? "))

    for bouncing_time in range(number_of_bounces):
        list_of_height.append(init_height)
        init_height = init_height / 2

    print(list_of_height)
    total_distance_travelled = sum(list_of_height) * 2 - 100
    print(f'The total distance travelled is {total_distance_travelled} meters.')
    print(f"The last height is {list_of_height[-1]}")



ball(100)