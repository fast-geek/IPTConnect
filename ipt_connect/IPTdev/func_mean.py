# All functions for calculating mean value are independent of other models, so don't use import

def mean(vec):
	return float(sum(vec)) / len(vec) if len(vec) != 0 else 0.0

def ipt_mean(vec):
	nreject = 1 if len(vec) in {5, 6} else (len(vec) + 3) >> 2
	# TODO: the following code looks messy, but it works.
	# There was an unsuccessful attempt to refactor it.
	# The code should be refactored and tested.

	nhigh = nreject / 2
	nlow = nreject - nhigh

	vec = vec[nlow : ] if nhigh == 0 else vec[nlow : -nhigh]
	return mean(vec)

def iypt_mean(vec):
    if len(vec) > 1 :
        vec.append((vec.pop(0) + vec.pop()) / 2.0)
        return mean(vec)
    return mean(vec)

def ttn_mean(vec):
	return mean(vec) if len(vec) <= 4 else iypt_mean(vec)
