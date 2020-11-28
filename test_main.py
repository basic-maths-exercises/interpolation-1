import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_graph(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==6, "The number of points in the graph is incorrect" )
        for i in range(6) :
            myx = xv[0]+i*(xv[1]-xv[0])/5
            self.assertTrue( np.abs(this_x[i] - myx  )<1e-7, "One or more of your x values are not correct" )
            myy = yv[0] + (this_x[i]-xv[0])*(yv[1]-yv[0]) / (xv[1]-xv[0])
            self.assertTrue( np.abs(this_y[i] - myy  )<1e-7, "One or more of your y values are not correct" )
