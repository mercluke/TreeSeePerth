class Converter:
    "Convert from one measurement to another"

    # assumption that the average person walks 5kms per hour
    # should make this a constant

    # time should be in minutes
    # distance returned in metres

    def timeToDist(time):
        return 5000 * (time / 60);


    # assume the average person takes 100 steps per minute.
    # Yes, I got that number off the internet
    def stepSizeToDist(stepSize, time):
        return (stepSize * 100) * time;

    # Should we also provide the user with a time estimate of
    # their walk if they select the distance option?
    # If they choose not to enter their own step size, we should
    # just put the default of 0.71m ??
