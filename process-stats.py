import glob
import os
import statistics

def printStats(list):
    avg = statistics.mean(list)
    med = statistics.median(list)
    mini = min(list)
    maxi = max(list)
    print("Average: ", avg)
    print("Median: ", med)
    print("Min: ", mini)
    print("Max: ", maxi)

#cache the stats in a local file
outFile = open("results.csv", "w")
outFile.write("name,numNeutral,numNegative,numPositive,perNeutral,perNegative,perPositive,\n")

# open all directories
for folder in glob.glob("**/"):
    #print(folder)
    # keep track of the total number of positive, neutral, and negative per folder
    totPositive = []
    totNeutral = []
    totNegative = []
    # get all files that end in .out in each folder
    for file in glob.glob(folder + "*.out"):
        #print(file)
        # keep track of the number of positive, neutral, and negative per file
        numPositive = 0
        numNeutral = 0
        numNegative = 0
        # open the file
        with open(os.path.join(file)) as f:
            # look at each line
            for line in f:
                if "neutral" in line:
                    numNeutral += 1
                elif "negative" in line:
                    numNegative += 1
                elif "positive" in line:
                    numPositive += 1
                #else: IGNORE

            #print("Number of Neutral: ", numNeutral)
            #print("Number of Negative: ", numNegative)
            #print("Number of Positive: ", numPositive)
            total = numNeutral + numNegative + numPositive
            perNeutral = (numNeutral / total) * 100
            perNegative = (numNegative / total) * 100
            perPositive = (numPositive / total) * 100
            #print("Percentage of Neutral: ", perNeutral)
            #print("Percentage of Negative: ", perNegative)
            #print("Percentage of Positive: ", perPositive)
            result = "{0},{1},{2},{3},{4},{5},{6},\n".format(file, numNeutral,
                numNegative, numPositive, perNeutral, perNegative, perPositive)
            outFile.write(result)
            totPositive.append(perPositive)
            totNeutral.append(perNeutral)
            totNegative.append(perNegative)

    print(folder)
    print("Neutral: ")
    printStats(totNeutral)
    print("Negative: ")
    printStats(totNegative)
    print("Positive: ")
    printStats(totPositive)

outFile.close()