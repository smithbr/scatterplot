import random


class Point():
	""" A Point represents a scatterplot point containing an
		[x, y] plot point.
	"""
	def __init__(self, x_point, y_point):
		self.x = x_point
		self.y = y_point


class Bounds():
	""" A Bounds represents a scatterplot containing a lower-left [x, y]
		boundary as well as an upper-right [x, y] boundary.
	"""
	def __init__(self, lower_left_boundary, upper_right_boundary):
		self.lower_left_boundary = lower_left_boundary
		self.upper_right_boundary = upper_right_boundary


class Plot():
	""" Evaluates plot points against the scatterplot's designated boundaries and
		prints the output into the shell.
	"""
	def __init__(self, boundaries, plot_points):
		self.boundaries = boundaries
		self.plot_points = plot_points
		self.RunEvaluation(self.boundaries, self.plot_points)


	def RunEvaluation(self, boundaries, plot_points):
		for plot_point in plot_points:
			print "Scatterplot boundaries: [x] %s and [y] %s" % (str(str(boundaries.lower_left_boundary.x) + ", " + str(boundaries.upper_right_boundary.x)), str(str(boundaries.lower_left_boundary.y) + ", " + str(boundaries.upper_right_boundary.y)))
			print "My plot [x, y]: %s, %s" % (plot_point.x, plot_point.y)
			if plot_point.x >= boundaries.lower_left_boundary.x and plot_point.x <= boundaries.upper_right_boundary.x and plot_point.y >= boundaries.lower_left_boundary.y and plot_point.y <= boundaries.upper_right_boundary.y:
				# If the plot is in boundaries...
				print "Passed! Your plot (%s) is in boundaries." % str(str(plot_point.x) + ", " + str(plot_point.y))
			else:
				print "Failed! Your plot is out of bounds.\nFail Reasons:"
				# If no conditions were met
				if plot_point.x < boundaries.lower_left_boundary.x or plot_point.x >= boundaries.upper_right_boundary.x or plot_point.y < boundaries.lower_left_boundary.y or plot_point.y >= boundaries.upper_right_boundary.y:
					# If X is out of boundaries
					if plot_point.x < boundaries.lower_left_boundary.x or plot_point.x >= boundaries.upper_right_boundary.x:
						print "Plot point [x] (%s) is not within the accepted range (%s, %s)." % (str(plot_point.x), str(boundaries.lower_left_boundary.x), str(boundaries.upper_right_boundary.x))
					# If Y is out of boundaries
					if plot_point.y < boundaries.lower_left_boundary.y or plot_point.y >= boundaries.upper_right_boundary.y:
						print "Plot point [y] (%s) is not within the accepted range (%s, %s)." % (str(plot_point.y), str(boundaries.lower_left_boundary.y), str(boundaries.upper_right_boundary.y))
				else:
					# How did we get here?
					print "Invalid plot value."
			print "\n"


if __name__ == '__main__':
	this_plots_boundaries = Bounds(Point(0,0), 	#Lower-left [x, y]
							Point(50,25)) 		#Upper-right [x. y]
	how_many_random_plots = 10
	largest_random_point = 100
	plot_points = []
	
	# Generate list of random plot points
	for plot in range(how_many_random_plots):
		plot_points.append(Point(random.randint(0, largest_random_point),random.randint(0, largest_random_point)))
	
	# Some additional boundary tests...
	# positive
	plot_points.append(Point(0,25))
	plot_points.append(Point(50,25))
	plot_points.append(Point(50,0))
	plot_points.append(Point(0,0))
	# negative
	plot_points.append(Point(51,26))
	plot_points.append(Point(-1,25))
	plot_points.append(Point(-1,26))
	plot_points.append(Point(50,-1))
	plot_points.append(Point(51,-1))
	plot_points.append(Point(-1,-1))
	plot_points.append(Point(0,-1))
	plot_points.append(Point(-1,0))

	# Evaluate our plots
	Plot(this_plots_boundaries, plot_points)
