# Practical-03: Fetching the training data from offline CSV resource
import numpy

# filename = open("C:\\Users\\shubh\\PycharmProjects\\MIS_DATA\\indians-diabetes.data.csv"))
filename = open("C:\\Users\\shubh\\PycharmProjects\\MIS_DATA\\indians-diabetes.data.csv")

data = numpy.loadtxt(filename, delimiter=",")

filename.close()

print("Numpy loadtxt Size = ", data.shape)
print("Data :\n", data)
