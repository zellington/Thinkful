r = 0

while r <=5:
	try:
		x = float(raw_input('Your number: '))
		inverse = 1.0 / x
	except ValueError:
		print "Don't be so dumb!"
	except ZeroDivisionError:
		print "Infinity"
	finally:
		print ('There may have been an error')
		print inverse
		r += 1