from proyect.CCProcessPDB import worksGraphs
import sys

matrixFullData = sys.argv[1]
pathOutput = sys.argv[2]

jobData = worksGraphs.jobsGraph(matrixFullData, pathOutput)
print "Get energetic matrix"
jobData.readMatrixData()
print "Create graph"
jobData.createGrphFromMatrix()
print "search elements"
jobData.searchSubGraphs()
