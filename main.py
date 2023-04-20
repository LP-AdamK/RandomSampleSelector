
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random as rnd


def sample_number(sampleT):
    sampleN = input("How many samples tested today?  ")

    #check that it is an integer
    try:
        sampleN = int(sampleN)
    except ValueError:
        print("sample must be a number")
        return

    #check that sampleN is <= list
    if(sampleN <= len(sampleT)):
        return sampleN
    else:
        print("not enough samples")
        return


def sample_type():
    sampleType = input("Which test method?  ")

    return sampleType
    # verify that its a real input.  Maybe we need options here
    # count the number of samples remaining in that list to compare to sampleN later


def make_selection():
    sampleNumber = rnd.choice(std_mylar)
    return sampleNumber


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create lists, right now these lists will reset all numbers of samples each time we run.

    std_mylar = [i for i in range(1, 45)]
    accel = [i for i in range(1, 45)]
    recyc = [i for i in range(1, 45)]
    no_hpp = [i for i in range(1, 25)]
    large_bag = [i for i in range(1, 25)]
    small_bag = [i for i in range(1, 25)]

    # Link lists to test type (accelerated, small, large etc)
    # ask for the number of samples and test type
    SN = sample_number(recyc)
    print(SN)
    # from appropriate list use random.choice() to select the right number of samples
    for i in range(1, SN+1):
        value = make_selection()
        print(f"Select sample number {value}.")

    # return the samples to the user
    # record date, samples selected and batch number in an excel file
    # print that excel file with spaces for results to fill in
    # remove samples from list


