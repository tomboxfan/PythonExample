# init variable
ant_speed = 10 # cm/s
rubber_band_speed = 5 # cm/s

ant_position = 0

# we need 2 variables to save rubber band position so that we know how many times rubber band has expanded
rubber_band_position_old = 100
rubber_band_position_new = 100

# we need 2 variables to save the distance between ant and rubber_band,
# so that we know whether the distance difference is getting smaller or not
# if it is not getting smaller, it means, the ant will never catch up with the rubber band head
distance_difference_old = rubber_band_position_old - ant_position
distance_difference_new = rubber_band_position_old - ant_position

time_unit = float(input("Please input time check unit:"))
print("We will check very %s second" % time_unit)

total_time_spent = 0

print("second later      ant position        rubber band head position")

# As long as the distance difference is greater than 0, it means the ant is still behind the rubber band head
while(distance_difference_new > 0):

    total_time_spent += time_unit

    # Step 1) Calculate where the rubber band head is after time_unit second
    rubber_band_position_new = rubber_band_position_old + rubber_band_speed * time_unit;

    # Step 2) Calculate where the ant is after time_unit second
    ant_position = ant_position + ant_speed * time_unit;

    # Step 3) Calculate how many times ant position should expand due to the expansion of the rubber band
    # it will expand the same times as the rubber band expands
    times = rubber_band_position_new / rubber_band_position_old
    ant_position = ant_position * times

    # Step 4) Check whether the ant can catch up with the rubber band head
    distance_difference_new = rubber_band_position_new - ant_position
    if distance_difference_old < distance_difference_new:
        print("After %0.3f second, the distance difference between ant and the rubber band head becomes %0.3f " % (time_unit, distance_difference_new))
        print("The ant is getting further to the head of the rubber band, the ant will never catch up with the rubber band head.")
        break

    # Step 6) Print result
    print("%0.3f        %0.3f        %0.3f " % (total_time_spent, ant_position, rubber_band_position_new ))

    # Step 7) Assign loop variables
    rubber_band_position_old = rubber_band_position_new
    distance_difference_old = distance_difference_new