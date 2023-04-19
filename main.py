
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random as rnd


def sample_number():
    sampleN = input("How many samples tested today?  ")
    #check if it's an integer
    #check that sampleN is <= list

def sample_type():
    sampleType = input("Which test method?  ")
    # verify that its a real input.  Maybe we need options here
    # count the number of samples remaining in that list to compare to sampleN later

def make_selection():
    rnd_num=rnd.random()
    yield rnd_num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create lists
    # Link lists to test type (accelerated, small, large etc)
    # ask for the number of samples and test type
    # from appropriate list use random.choice() to select the right number of samples
    # return the samples to the user
    # record date, samples selected and batch number in an excel file
    # print that excel file with spaces for results to fill in
    # remove samples from list
    for value in make_selection():
        print(value)

